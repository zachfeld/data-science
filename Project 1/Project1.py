import pandas as pd

## import data
election_2016 = pd.read_csv('election_2016.csv')
covid_county = pd.read_csv('covid_confirmed_usafacts.csv')
population_county = pd.read_csv('covid_county_population_usafacts.csv')

## Group data by State, not county
covid_state = covid_county.groupby('State').sum()
population_state = population_county.groupby('State').sum()

## Merging all the three datasets into one big data frame
state_election_covid = pd.DataFrame(population_state.merge(election_2016, on='State').merge(covid_state, on='State'))

## Removing county-specific columns (2)
exclude_counties = ['countyFIPS_x', 'countyFIPS_y']
state_election_covid = state_election_covid.loc[:, ~state_election_covid.columns.isin(exclude_counties)]
print(state_election_covid)






## Export to Excel for viewing
#state_election_covid.to_excel(r'Project 1\state_election_covid.xlsx')
