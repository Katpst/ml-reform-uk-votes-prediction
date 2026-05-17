# Data Sources

This project combines UK election results with constituency-level demographic and socioeconomic data for the 650 (607 after filtering) Westminster parliamentary constituencies used in the 2024 General Election.

## 1. 2024 General Election Results
- **Source:** UK Parliament (House of Commons Library)
- **File:** `HoC-GE2024-results-by-constituency.csv`
- **URL:** https://commonslibrary.parliament.uk/research-briefings/cbp-10009/
- **Variable:** `reform_vote_share`
- **Description:** Reform UK vote share calculated as Reform UK votes divided by total valid votes.

## 2. Brexit Referendum Estimates on 2024 boundaries
- **Source:** Chris Hanretty (2024 boundary estimates)
- **File:** `2016_Brexit_referendum_estimates_on_2024_boundaries.csv`
- **URL:** https://docs.google.com/spreadsheets/d/1mtph-ml7CYVoeEUIc1g_IbOvbiZMa_ezRGQlHQoCpF4/edit
- **Variable:** `leave_vote_share`
- **Description:** Model-based estimates of the 2016 EU referendum Leave vote share
mapped to the 2024 constituency boundaries. These are estimates, not official results,
because the referendum was counted at local authority level and not the constituency level.

## 3. Census Qualifications Data
- **Source:** House of Commons Library Constituency Data
- **Files:** `Qualifications_census.xlsx`
- **URL:** https://commonslibrary.parliament.uk/research-briefings/cbp-10576/
- **Variable Created:** `degree_pct`
- **Description:** Percentage of residents with degree-level qualifications or above.

## 4. Census Demographic Data
- **Source:** House of Commons Library (2021/2022 Census data)

### Age and population
- **File:** `CBP-10529.xlsx`
- **URL:** https://commonslibrary.parliament.uk/research-briefings/cbp-10529/
- **Variables:** `median_age`, `population_density`
- **Description:** Population by age at constituency level.
Median age computed as a weighted median from the age distribution.
Population density derived by dividing total population by constituency
area in km² from the ONS boundary file.

### Country of birth
- **File:** `country_of_birth_census.xlsx`
- **URL:** https://commonslibrary.parliament.uk/research-briefings/cbp-10581/
- **Variable:** `log_foreign_born_pct`
- **Description:** Share of residents born outside the UK (EU and rest of world
combined), log-transformed.

### Ethnicity
- **File:** `CBP-10566.xlsx`
- **URL:** https://commonslibrary.parliament.uk/research-briefings/cbp-10566/
- **Variable:** `ethnic_minority_pct`
- **Description:** Share of residents identifying as non-White.

## 5. Labour Market Data
- **Source:** House of Commons Library/ONS

### Median weekly wage
- **File:** `ONS-median-wages.xlsx`
- **URL:** https://www.ons.gov.uk/employmentandlabourmarket/peopleinwork/earningsandworkinghours/bulletins/annualsurveyofhoursandearnings/2024
- **Variable:** `median_weekly_wage`
- **Description:** Median gross weekly pay for full-time employees at
constituency level, sourced from the ONS Annual Survey of Hours and Earnings.

### Claimant rate
- **File:** `claimant_count.xlsx`
- **URL:** https://www.nomisweb.co.uk/query/construct/summary.asp?mode=construct&version=0&dataset=162
- **Variable:** `claimant_rate`
- **Description:** Number of people claiming Jobseeker's Allowance and required to seek work, expressed as a percentage of residents aged 16-64.

## 6. Index of Multiple Deprivation (IMD)
- **Source:** UK Constituency Data Hex Maps
- **File:** `parl24_imd.csv`
- **URL:** https://hex.constituencies.org.uk/themes/society/imd/
- **Variable:** `deprivation_score`
- **Description:** UK-wide composite deprivation score where higher values indicate greater deprivation.