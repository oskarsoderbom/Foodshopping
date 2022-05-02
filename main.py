"""Testing the foodscripts"""
from shopping import fillshoppinglist
from ingredients import several_recipes

def main():

    manyrecipes = ['https://undertian.com/recept/pasta-med-ajvar-relish-och-aubergine/'
    , 'https://undertian.com/recept/potatispaj-med-dill-och-tangkaviar/',
    'https://undertian.com/recept/havrerisbiffar-med-fetaost-i-pitabrod/',
    'https://undertian.com/recept/kramig-belugapastasas-med-paprika/']

    onerecipe = ['https://undertian.com/recept/kramig-belugapastasas-med-paprika/']

    fillshoppinglist(several_recipes(manyrecipes))

if __name__ == "__main__";
    main()
