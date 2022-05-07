"""Testing the foodscripts"""
from shopping import fillshoppinglist
from recipeselection import read_data, select_random_recipes
from ingredientsretrieve import get_all_ingredients

def main() -> None:
    "Calling all functions"

    recipelist = read_data('/Users/oskarsoderbom/Downloads/recipes - recipes-3.csv')
    randomrecipelist, allrecipes = select_random_recipes(recipedata=recipelist, n_fish=1, n_chicken=1, n_meat=1, n_veg=2)

    print(allrecipes)

    print()


    fillshoppinglist(get_all_ingredients(randomrecipelist))

if __name__ == "__main__":
    main()
