#placeholder Moles to grams calculator
from ChemDatabase import elemental_prefix_list
from ChemDatabase import elemental_weight_list

def MolesToGrams(Moles):
    print("What element do you have: ")
    Prefix = input()
    y = elemental_prefix_list.index(Prefix)
    z = elemental_weight_list[y]
    g = int(Moles)
    x = g*z

    return(print("The amount of grams you have is equal to: ", x))