"""Functions used in order to retrieve ingredients data"""

import requests
from bs4 import BeautifulSoup


def get_undertian(recipeurl: str) -> list:
    """Retrieves recipeingredients from undertian """

    url = recipeurl
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    results = soup.find(class_="recept-box recept-ingredients")
    ingredients_box = results.find_all(name='script')
    startlist = list(ingredients_box)
    manylists = [element for item in startlist[0] for element in item.split('{')]

    rough_ingredients = []

    for count, value in enumerate(manylists):
        tmp_list = []
        if manylists[count][1] == 'a':
            tmp_list.append(value.replace('"', "").
                                    replace("}", "").
                                    replace('amount:', "").
                                    replace('unit:', "").
                                    replace('type:', "").
                                    replace('alternative:', "").
                                    replace("\\u00f6", 'ö').
                                    replace("\\u00e5", 'å').
                                    replace("\\u00e4", 'ä').
                                    replace("\\u00e9", "è").
                                    replace("att steka i", "").
                                    replace("Salt &", "").
                                    replace("Olja", ""))

            rough_ingredients.append(tmp_list)

    cleaner = []
    for i in rough_ingredients:
        roughlist = i[0].split(",")
        cleaner.append(roughlist)

    del cleaner[len(cleaner)-1][4:]

    fooditems = [row[2] for row in cleaner]
    return fooditems



def get_koket(recipeurlkoket: str) -> list:
    """Scraping recipeingredients from koket.se"""
    url = recipeurlkoket
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    results = soup.find(class_="ingredients_ingredientList__YkFJY")
    ingredients_box = list(results.find_all(class_='ingredient'))


    new_list = []
    for i in ingredients_box:
        x = str(i).replace('<span class="ingredient"><span>', "").replace('<!-- --> <!-- -->'," ").replace('</span></span>',"").replace("<!-- -->"," ")
        new_list.append(x)
        
    return new_list

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



def get_all_ingredients(listofrecipes: list) -> list:

    '''Retrieves all ingredients from different websites'''
    all_ingredients = []

    for recipe in listofrecipes:
        
        if 'undertian' in recipe:
            tmpundertian = get_undertian(recipe)

            all_ingredients.append(tmpundertian)
        
        if 'koket.se' in recipe:
            tmpkoket = get_koket(recipe)

            all_ingredients.append(tmpkoket)

        if 'ica.se' in recipe:
            tmpica = get_ica(recipe)

            all_ingredients.append(tmpica)

    flat_list = [item for sublist in all_ingredients for item in sublist]

    return flat_list


