from ChemDatabase import elemental_weight_list
from ChemDatabase import elemental_prefix_list
def Find_Atomic_Weight(Prefix):
    x = elemental_prefix_list.index(Prefix)
    elemental_weight_list[x]
    return(print("The element: ", Prefix, " has a g/Mol ratio of: ", elemental_weight_list[x])) 
