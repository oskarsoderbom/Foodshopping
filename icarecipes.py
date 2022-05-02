import requests
from bs4 import BeautifulSoup

def get_ica(recipeurlica: str) -> list:
    """Scraping recipeingredients from ica.se"""
    url = recipeurlica 
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    results = soup.find(class_="ingredients-list-group row-noGutter-column")
    ingredients_box = list(results.find_all(class_='ingredients-list-group__card__ingr'))


    new_list = []
    for i in range(0, len(ingredients_box), 1):
        x = str([element for item in ingredients_box[i] for element in item.split("</span>")])
        new_list.append(x.replace("'\\n        ","").
                            replace("\\n      '", "").
                            replace("[", "").replace("]",""))
    
    return new_list

twoicarecipes = ['https://www.ica.se/recept/pasta-med-tomatsas-och-mozzarella-726242/', 'https://www.ica.se/recept/klassiska-kottbullar-712807/']

def several_recipes_ica(recipelist: list) -> list:
    """Takes a list of recipes, retrieves all the ingredients 
    and do some datacleaning + listflattening which will be used as input to
    the automatic webshopping"""

    all_items = []

    for recipe in recipelist:
        itemlist = get_ica(recipe)
        all_items.append(itemlist)
    
    #Flattens the list
    flat_list = [item for sublist in all_items for item in sublist] 
    
    #Getting rid of duplicates for now, should be handled accordingly later on
    #shoppinglist = list(set(flat_list))
    return flat_list

