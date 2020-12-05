# Pokemon Data Exploration Project
The purpose of this project was to explore the Complete Pokemon Dataset, analyze the data for correlations between Pokemon size and its stats, 
and create a fun dashboard application where users could see which Pokemon most resemble their size. 
The most obvious conclusion from our data analysis is that there is a clear correlation between a Pokemon’s height and weight. 
However, the correlations between a Pokemon’s size and the rest of its combat stats (HP, Attack, Special Attack, Defense, and Special Defense) are much more mixed, even after controlling for the Pokemon’s legendary status. 
# Where did our data come from?
## [Published Deepnote Project](https://deepnote.com/publish/566c903d-0732-4280-ab72-4ef957376f69)
The data used came from “The Complete Pokemon Dataset” on Kaggle uploaded by user Rounak Banik. Last updated 3 years ago, 
it contains all 801 Pokemon up to Generation 7, therefore not including Generation 8 Pokemon from the latest Pokemon Sword and Shield titles. 
The dataset also contains 40 columns, 18 of which are the effectiveness of different type moves against that Pokemon. 
(e.g. Flying-type moves have a 2x effectiveness against Bulbasaur) While we did not use these type-effectiveness variables, 
we did find many of the other variables useful for our data analysis and dashboard application. 
Other than name, each Pokemon is uniquely identified by its Pokedex number, 
which is a number that uniquely identifies a Pokemon species within the in-game handheld digital Pokemon compendium/encyclopedia. 
Since the Pokedex number takes a range of values from 1 to 801 for all 801 Pokemon, 
it was easy to treat the Pokedex number as an index value to identify individual Pokemon in our code, 
which was also useful when assigning each Pokemon its picture from PokeAPI.

The data was easy to work with. The only cleaning involved required dropping twenty rows in which the Pokemon had missing values for their height and weight. 
This was necessary to produce our correlation heatmaps.
# Analysis Results
In the first correlation heatmap, other than the obvious connection between height and weight, 
there were weak to moderately-strong correlations between height and weight and the rest of the variables, 
with the exceptions of between height and speed, and weight and speed.
We thought that perhaps these correlations could be skewed by Legendary Pokemon, 
Pokemon that are very rare and extremely powerful and therefore boast much higher stats compared to regular Pokemon, 
but aren’t necessarily larger. Fortunately, the dataset had a boolean variable “is_legendary” that made it very easy to subset by legendary status. 
We thought that perhaps subsetting by legendary status would lead to stronger correlations in either or both of the two groups.

However, this wasn't the case. It seems most of the correlations became weaker across the board. In some cases, the correlations approached close to 0, 
such as weight and speed for non-legendary Pokemon and weight and special defense for legendary Pokemon.

There were some notable exceptions, however. The correlation between weight and attack became stronger for non-legendary Pokemon, 
and weight and speed became a moderately-strong negative correlation for legendary Pokemon.
# Interactive Dashboard Component
## [Streamlit Dashboard!](https://blooming-beyond-75995.herokuapp.com/) | [Code Repository!](https://github.com/zfeldman7/pokemon-size-dashboard)
The goal of our dashboard was to create a dashboard application where users could enter their height and weight and view the Pokemon that closest matched their size. We wanted to show an image of the Pokemon along with its basic information in the return query, but since our original dataset didn’t contain any images, we had to pull requests from PokeAPI to retrieve the website links to each Pokemon’s ingame sprite. PokeAPI is an API linked to a database containing vast information about essentially everything within the Pokemon games. For each Pokemon in our data set, we can request a URL from PokeAPI pointing to a sprite for that Pokemon.

