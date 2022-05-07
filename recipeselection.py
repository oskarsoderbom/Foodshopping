
"""Reading recipes, selecting random recipes based on user input"""

import pandas as pd


def read_data(path: str) -> pd.DataFrame:
    """ Reading recipes
    this should be redone to read directly from google drive"""
    recipes = pd.read_csv(path)
    return recipes

def select_random_recipes(recipedata: pd.DataFrame, n_fish: int,
                                 n_meat: int, n_veg: int, n_chicken: int) -> pd.DataFrame:
    """Selects random recipes from a dataset with recipe names and links
    User defined number of different recipes"""

    fishrec = recipedata[recipedata['Type'] == 'Fish']
    vegrec = recipedata[recipedata['Type'] == 'Veg']
    chickenrec = recipedata[recipedata['Type'] == 'Chicken']
    meatrec = recipedata[recipedata['Type'] == 'Meat']

    fish_random = fishrec.sample(n = n_fish)
    chicken_random = chickenrec.sample(n = n_chicken)
    meat_random = meatrec.sample(n = n_meat)
    veg_random = vegrec.sample(n = n_veg)


    all_rand_recipes = pd.concat([fish_random, chicken_random, meat_random, veg_random])

    all_random_recipes_links = all_rand_recipes['Länk'].to_list()
    return all_random_recipes_links, all_rand_recipes

