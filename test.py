"""Testing the foodscripts"""
from webauto import fillshoppinglist
from webtest import several_recipes






manyrecipes = ['https://undertian.com/recept/pasta-med-ajvar-relish-och-aubergine/'
, 'https://undertian.com/recept/potatispaj-med-dill-och-tangkaviar/',
'https://undertian.com/recept/havrerisbiffar-med-fetaost-i-pitabrod/',
'https://undertian.com/recept/kramig-belugapastasas-med-paprika/']

onerecipe = ['https://undertian.com/recept/kramig-belugapastasas-med-paprika/']

fillshoppinglist(several_recipes(onerecipe))
