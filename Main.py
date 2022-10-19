from g_mol_finder import Find_Atomic_Weight
from MolesToGrams import MolesToGrams

FuncF = [Find_Atomic_Weight, MolesToGrams]

print("What do you want to do?")
print("1: Find Atomic Weight?")
print("2. Find Grams from Moles?")

g = int(input())-1 
if g == 0:
    x = input("Enter your chosen element here: ")
    Find_Atomic_Weight(x)
if g == 1:
    y = input("enter the amount of Moles you need here: ")
    MolesToGrams(y)
