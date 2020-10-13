import pandas as pd
import random
import numpy as np
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

# pickle our dataset here
df.to_pickle('project-1-dataset.pkl')

# ~~~~~~   Question 4 - Applying a SciPy's curve fit function   ~~~~~~
## Apply SciPy curve_fit function to each row, returning three beta values for each row,
## and create three columns for those three beta values
def logistic_curve ( x, β0, β1, β2 ):
    # β0 - max # of cases in long term
    # β1 - measure of the rate of spread
    # β2 - time of maximum spread
    return β0 / (1 + np.exp(β1 * (-x + β2) ) )

def bad_guess (data):
    # β0 - max number of cases seen so far
    # β1 - 1
    # β2 - date range / 2
    date_rows = data.iloc[:,3:]
    
    # make guesses based on the criteria listed above
    data['β0'] = date_rows.max(axis=1)
    data['β1'] = [1] * len(data)
    data['β2'] = (len(date_rows.columns) / 2)

    return data

from scipy.optimize import curve_fit
import  matplotlib.pyplot as plt

# put all of our guessed betas into the dataframe
data = bad_guess(df)

# create new dataframe to store found betas in
new_betas = pd.DataFrame(data.index)
new_betas = new_betas.set_index('State')

# loop through every state in the data frame
indicies = data.index
for index in indicies:

    state = data.loc[index]

    # get the guessed betas, xs and ys
    my_guessed_betas = [state.loc['β0'], state.loc['β1'], state.loc['β2']]
    xs = np.arange(0,len(state)-6)
    ys = state.iloc[3:len(state)-3]

    # fit the logistic curve to the data, if we can't throw an exception
    try:

        found_betas, covariance = curve_fit( logistic_curve, xs, ys.astype('int'), p0=my_guessed_betas )
        β0, β1, β2 = found_betas
        print(f'{index} ', covariance) # add state to print along covariance
        new_betas.loc[index, 'β0'] = β0
        new_betas.loc[index, 'β1'] = β1
        new_betas.loc[index, 'β2'] = β2
    except Exception as e:
        print(f'state: {index}: ', e)
        pass
#print(new_betas)
# ~~~~~~   Question 5 - Correlation between political leaning and variables   ~~~~~~
# for problem 5, we need to make a dataframe with pop, clinton, trump, all 3 of the calculated b's, 
# most recent number of cases, most recent number of cases per cap, political leaning ratio
corr_data = pd.DataFrame(data.index)
corr_data = corr_data.set_index('State')
### population column (for per capita)
corr_data['Population'] = df['population']
### political leaning
corr_data['D/R Ratio'] = round(df['Clinton'] / df['Trump'], 3)
### most recent number of cases + per capita
corr_data['Recent Cases'] = df['9/8/20'] # change to a not hard-coded column value later
corr_data['Recent Cases per Capita'] = round(corr_data['Recent Cases'] / corr_data['Population'] * 1000000, 3) # multiply by 1 mil, per 1 mil people
### Projected Max Number of Cases = β0, and capita
corr_data['Projected Max Cases'] = new_betas['β0']
corr_data['Projected Max Cases per Capita'] = round(corr_data['Projected Max Cases'] / corr_data['Population'] * 1000000, 3)
### rate of increase = β1
corr_data['Rate of Increase'] = new_betas['β1']
### time of maximum increase = β2
corr_data['Time of maximum increase'] = new_betas['β2']



corr_data = corr_data.drop('Population', axis=1)
corr_data = corr_data.drop(['HI'])
correlation_coefficients = np.corrcoef( corr_data, rowvar=False )

# the graphing is commented out here to not pause the script on run
'''
import seaborn as sns
plt.figure(figsize=(12,8))
sns.heatmap( correlation_coefficients, annot=True )
plt.xticks( np.arange(7)+0.5, corr_data.columns, rotation = 35 )
plt.yticks( np.arange(7)+0.5, corr_data.columns, rotation = 0 )
plt.show()
'''


# ~~~~~~   Question 6 - Hypothesis test    ~~~~~~
# We are testing for the difference in mean number of days of max increase/spread between democratic and republican states
# This is a two sided test, where our first sample is the democratic states' beta 2 (time of max spread)
# And our second sample is the republican states' beta 2

α = 0.05
# boiling down our data set to the democratic & republican leaning states
dem_leaning = corr_data[corr_data['D/R Ratio'] > 1]
gop_leaning = corr_data[corr_data['D/R Ratio'] < 1]

sample1 = dem_leaning['Time of maximum increase']
sample2 = gop_leaning['Time of maximum increase']

import scipy.stats as stats
t_statistics, p_value = stats.ttest_ind(sample1, sample2)

reject_H0 = p_value < α
print(α, p_value, reject_H0)

# Our output is [0.05 2.5011897072328965e-05 True]
# Therefore, we can say that the two samples give us enough information to reject H0
# Democratic and Republican states have different means time of maximum increase since the pandemic started
