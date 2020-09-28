'''
Add a Python script or Jupyter notebook to your Project 1 repository.

In that script or notebook, write a Python function that behaves as follows:

- It takes as input the abbreviation of a state in the U.S., such as "MA" or "TX".
- It returns as output a pandas Series of the number of confirmed cases of COVID-19 in that state over time.

Submit your work by committing and pushing to the repository. I will be able to see it because you have already invited me to the repository as a collaborator.
'''
import pandas as pd

covid_county = pd.read_csv('covid_confirmed_usafacts.csv')

# Group all counties by state
covid_state = covid_county.groupby('State').sum()

# Remove countyFIPS and stateFIPS columns
exclude_columns = ['countyFIPS', 'stateFIPS']
covid_state = covid_state.loc[:, ~covid_state.columns.isin(exclude_columns)]

# function takes state as string argument and returns pandas series 
def confirmed_covid(state):
    return covid_state.loc[state] 

print(confirmed_covid('NJ'))