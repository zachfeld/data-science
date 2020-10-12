import pandas as pd

## import data
election_2016 = pd.read_csv('election_2016.csv')
covid_county = pd.read_csv('covid_confirmed_usafacts.csv')
population_county = pd.read_csv('covid_county_population_usafacts.csv')

# ~~~~~~~   Question 3 - Creating a united Pandas DataFrame   ~~~~~~
## Group data by State, not county
covid_state = covid_county.groupby('State').sum()
population_state = population_county.groupby('State').sum()

## Merging all the three datasets into one big data frame
df = pd.DataFrame(population_state.merge(election_2016, on='State').merge(covid_state, on='State'))

## Setting index to the state code
df = df.set_index('State')

## Removing FIPS columns (3)
exclude_counties = ['countyFIPS_x', 'countyFIPS_y', 'stateFIPS']
df = df.loc[:, ~df.columns.isin(exclude_counties)]
#print(df.columns)


# ~~~~~~   Question 4 - Applying a SciPy's curve fit function   ~~~~~~
## Apply SciPy curve_fit function to each row, returning three beta values for each row,
## and create three columns for those three beta values
import math
def my_model ( x, β0, β1, β2 ):
    # β0 - max # of cases in long term
    # β1 - measure of the rate of spread
    # β2 - time of maximum spread
    return β0 / (1 + math.exp(β1 * (-x + β2) ) )

## Export to Excel for viewing
#df.to_excel(r'Project 1\state_election_covid.xlsx')
