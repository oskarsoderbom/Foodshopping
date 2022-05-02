"""Testing the foodscripts"""
from shopping import fillshoppinglist
from ingredients import several_recipes
from icarecipes import get_ica

def main() -> None:
    "Calling all functions"

    manyrecipes = ['https://undertian.com/recept/pasta-med-ajvar-relish-och-aubergine/'
    , 'https://undertian.com/recept/potatispaj-med-dill-och-tangkaviar/',
    'https://undertian.com/recept/havrerisbiffar-med-fetaost-i-pitabrod/',
    'https://undertian.com/recept/kramig-belugapastasas-med-paprika/']

    onerecipe = ['https://undertian.com/recept/kramig-belugapastasas-med-paprika/']
    icarecipe = 'https://www.ica.se/recept/klassiska-kottbullar-712807/'
    fillshoppinglist(get_ica(icarecipe))

if __name__ == "__main__":
    main()
