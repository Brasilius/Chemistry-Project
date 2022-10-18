from ChemDatabase import elemental_weight_list
from ChemDatabase import elemental_prefix_list
def Find_Atomic_Weight(Prefix):
    Prefix = str.input()
    for Prefix in elemental_prefix_list:
        x = elemental_prefix_list.index(Prefix)
        elemental_weight_list[x]
        return(str.print("The element: ", Prefix, " has a g/Mol ratio of: ", elemental_weight_list[x])) 
Find_Atomic_Weight()