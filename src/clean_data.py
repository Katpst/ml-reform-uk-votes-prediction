from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
PROCESSED = ROOT / "data" / "processed"
PROCESSED.mkdir(parents=True, exist_ok=True)


# Election data
election = pd.read_csv(RAW / "HoC-GE2024-results-by-constituency.csv")
election = election[["Constituency name", "Valid votes", "RUK"]].copy()
election["reform_vote_share"] = 100 * election["RUK"] / election["Valid votes"]
election = election.rename(columns={"Constituency name": "constituency"})
election = election[["constituency", "reform_vote_share"]]
election.to_csv(PROCESSED / "reform_vote_share.csv", index=False)


# Brexit estimates (2024 boundaries)
brexit = pd.read_csv(RAW / "2016_Brexit_referendum_estimates_on_2024_boundaries.csv")
brexit = brexit[["Constituen", "LeavePct"]].copy()
brexit = brexit.rename(columns={"Constituen": "constituency", "LeavePct": "leave_vote_share"})
brexit["leave_vote_share"] = pd.to_numeric(brexit["leave_vote_share"], errors="coerce")
if brexit["leave_vote_share"].max() <= 1:
    brexit["leave_vote_share"] *= 100
brexit = brexit.dropna(subset=["leave_vote_share"])
brexit.to_csv(PROCESSED / "leave_vote_share.csv", index=False)


# Education - degree share
def extract_education(sheet_name, category_col, category_value):
    df = pd.read_excel(RAW / "Qualifications_census.xlsx", sheet_name=sheet_name)
    df = df[df[category_col] == category_value].copy()
    df = df[["ConstituencyName", "Con_pc"]].copy()
    df = df.rename(columns={"ConstituencyName": "constituency", "Con_pc": "degree_pct"})
    df["degree_pct"] = df["degree_pct"] * 100
    return df

edu_ew = extract_education("EW_constituencies", "groups", "Higher education qualifications")
edu_ni = extract_education("NI_constituencies", "groups", "Higher education qualifications")
edu_scotland = extract_education("Scotland_Constituencies", "Groups", "Degree level qualifications or above")
education = pd.concat([edu_ew, edu_ni, edu_scotland], ignore_index=True)
education.to_csv(PROCESSED / "degree_pct.csv", index=False)


# Median age
age_raw = pd.read_excel(RAW / "CBP-10529.xlsx", sheet_name="Single year of age")

def weighted_median_age(group):
    group = group.sort_values("age").copy()
    total_pop = group["con_number"].sum()
    group["cum_pop"] = group["con_number"].cumsum()
    return group.loc[group["cum_pop"] >= total_pop / 2, "age"].iloc[0]

median_age = (
    age_raw
    .groupby("con_name")
    .apply(weighted_median_age, include_groups=False)
    .reset_index(name="median_age")
)
median_age = median_age.rename(columns={"con_name": "constituency"})
median_age.to_csv(PROCESSED / "median_age.csv", index=False)


# Median weekly wage
wages = pd.read_excel(RAW / "CBP-10524.xlsx", sheet_name="Data")
wages = wages[["ConstituencyName", "Constituency"]].copy()
wages = wages.rename(columns={"ConstituencyName": "constituency", "Constituency": "median_weekly_wage"})
wages.to_csv(PROCESSED / "median_weekly_wage.csv", index=False)


# Claimant rate
claimant = pd.read_excel(RAW / "claimant_count_2026-03-19_09-29-28.xlsx", sheet_name="Sheet 1")
claimant = claimant[["ConstituencyName", "Constituency rate"]].copy()
claimant = claimant.rename(columns={"ConstituencyName": "constituency", "Constituency rate": "claimant_rate"})
claimant["claimant_rate"] = claimant["claimant_rate"] * 100
claimant.to_csv(PROCESSED / "claimant_rate.csv", index=False)


# Foreign-born share (EU + rest of world)
birth = pd.read_excel(RAW / "country_of_birth_census.xlsx", sheet_name="Constituency - groups")
birth = birth[birth["groups"].isin(["European Union", "Rest of world"])].copy()
birth = birth.groupby("ConstituencyName", as_index=False)["con_pc"].sum()
birth = birth.rename(columns={"ConstituencyName": "constituency", "con_pc": "foreign_born_pct"})
birth["foreign_born_pct"] = birth["foreign_born_pct"] * 100
birth.to_csv(PROCESSED / "foreign_born_pct.csv", index=False)


# Population density
population = age_raw.groupby("con_name", as_index=False)["con_number"].sum()
population.columns = ["constituency", "population"]

area = pd.read_csv(RAW / "Westminster_Parliamentary_Constituencies_July_2024_Boundaries_UK.csv")
area = area[["PCON24NM", "Shape__Area"]].copy()
area.columns = ["constituency", "shape_area_m2"]
area["area_sq_km"] = area["shape_area_m2"] / 1_000_000
area = area[["constituency", "area_sq_km"]]

density = population.merge(area, on="constituency", how="inner")
density["population_density"] = density["population"] / density["area_sq_km"]
density = density[["constituency", "population", "area_sq_km", "population_density"]]
density.to_csv(PROCESSED / "population_density.csv", index=False)


# Ethnic minority share
ethnicity = pd.read_excel(RAW / "CBP-10566.xlsx", sheet_name="Ethnic groups - broad")
ethnicity = ethnicity[ethnicity["groups"] == "White"].copy()
ethnicity["ethnic_minority_pct"] = (1 - ethnicity["con_pc"]) * 100
ethnicity = ethnicity[["ConstituencyName", "ethnic_minority_pct"]].copy()
ethnicity = ethnicity.rename(columns={"ConstituencyName": "constituency"})
ethnicity.to_csv(PROCESSED / "ethnic_minority_pct.csv", index=False)


# Deprivation score (IMD)
imd = pd.read_csv(RAW / "parl24_imd.csv")
imd = imd[["constituency-name", "parl25-deprivation-score"]].copy()
imd = imd.rename(columns={"constituency-name": "constituency", "parl25-deprivation-score": "deprivation_score"})
imd.to_csv(PROCESSED / "deprivation_score.csv", index=False)


# Merge all into model dataset
def clean_name(s):
    return (
        s.astype(str)
        .str.replace("&", "and", regex=False)
        .str.replace("ï¿½", "ô", regex=False)
        .str.strip()
        .str.lower()
    )

files = {
    "reform": "reform_vote_share.csv",
    "brexit": "leave_vote_share.csv",
    "education": "degree_pct.csv",
    "age": "median_age.csv",
    "wages": "median_weekly_wage.csv",
    "claimant": "claimant_rate.csv",
    "foreign_born": "foreign_born_pct.csv",
    "density": "population_density.csv",
    "ethnicity": "ethnic_minority_pct.csv",
    "deprivation": "deprivation_score.csv",
}

dfs = {}
for name, file in files.items():
    df = pd.read_csv(PROCESSED / file)
    df["constituency_key"] = clean_name(df["constituency"])
    df = df.drop_duplicates(subset=["constituency_key"], keep="first")
    dfs[name] = df

model_data = dfs["reform"].copy()
for name, df in dfs.items():
    if name == "reform":
        continue
    feature_cols = [c for c in df.columns if c not in ["constituency", "constituency_key"]]
    model_data = model_data.merge(df[["constituency_key"] + feature_cols], on="constituency_key", how="left")

model_data = model_data.drop(columns=["constituency_key", "population", "area_sq_km"])
model_data = model_data.dropna()

print(model_data.shape)
print(model_data.isna().sum())

model_data.to_csv(PROCESSED / "model_data.csv", index=False)