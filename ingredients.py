"""Functions used in order to retrieve ingredients data"""


from bs4 import BeautifulSoup
import requests

def get_recipe_ingredients(recipeurl: str) -> list:
    """Function used to take a list of recipeurls and return all 
    Right now working for undertian.com
    """

    if recipeurl.__contains__('undertian'):
        url = recipeurl
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")

        # Alternativt sätt att göra det på, kan behöva justeras lite om det finns flera
        # 'receptgrupper'.
        MEASUREMENTS = ["dl", "st", "msk", "tsk", "port"]
        ingredient_spans = soup.find_all("span", {"itemprop": "recipeIngredient"})
        ingredients = []
        for ing in ingredient_spans:
            ing_raw: str = ing.text
            measurements_mentioned = [m for m in ing_raw.split() if m.lower() in MEASUREMENTS]
            if measurements_mentioned:
                measurement = measurements_mentioned[0]
                measurement_index = ing_raw.find(measurement)
            
                try:
                    amount = float("".join(ing_raw[:measurement_index].split()))
                except ValueError:
                    amount = 0.0

                desc = ing_raw[measurement_index+len(measurement):].strip()
                ingredients.append(
                    {"amount": amount,
                    "measurement": measurement,
                    "description": desc}
                )

        results = soup.find(class_="recept-box recept-ingredients")
        ingredients_box = results.find_all(name='script')
        startlist = list(ingredients_box)
        manylists = [element for item in startlist[0] for element in item.split('{')]

        rough_ingredients = []

        for count, value in enumerate(manylists):
            tmp_list = []
            if manylists[count][1] == 'a':
                tmp_list.append(value.replace('"',"").
                                        replace("}", "").
                                        replace('amount:', "").
                                        replace('unit:',"").
                                        replace('type:', "").
                                        replace('alternative:', "").
                                        replace("\\u00f6", 'ö').
                                        replace("\\u00e5", 'å').
                                        replace("\\u00e4",'ä').
                                        replace("\\u00e9","è").
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


def several_recipes(recipelist: list) -> list:
    """Takes a list of recipes, retrieves all the ingredients 
    and do some datacleaning + listflattening which will be used as input to
    the automatic webshopping"""

    all_items = []

    for recipe in recipelist:
        itemlist = get_recipe_ingredients(recipe)
        all_items.append(itemlist)
    
    #Flattens the list
    flat_list = [item for sublist in all_items for item in sublist] 
    
    #Getting rid of duplicates for now, should be handled accordingly later on
    #shoppinglist = list(set(flat_list))
    return flat_list

