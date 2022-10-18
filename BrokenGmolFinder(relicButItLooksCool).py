from ast import Constant
from dataclasses import dataclass
from sys import prefix
import DataStorageForElements
print ("Enter the prefix of your element in all caps: ")
Prefix_1 = input()
def MolecularWeightGiver(Prefix_1):
    m1 = Prefix_1
    if m1 == "H":
        print(DataStorageForElements.element_weight_list[0])
    if m1 == "HE":
        print(DataStorageForElements.element_weight_list[1])
    if m1 == "LI":
        print(DataStorageForElements.element_weight_list[2])
    if m1 == "BE":
        print(DataStorageForElements.element_weight_list[3])
    if m1 == "B":
        print(DataStorageForElements.element_weight_list[4])
    if m1 == "C":
        print(DataStorageForElements.element_weight_list[5])
    if m1 == "N":
        print(DataStorageForElements.element_weight_list[6])
    if m1 == "O":
        print(DataStorageForElements.element_weight_list[7])
    if m1 == "F":
        print(DataStorageForElements.element_weight_list[8])
    if m1 == "NE":
        print(DataStorageForElements.element_weight_list[9])
    if m1 == "NA":
        print(DataStorageForElements.element_weight_list[10])
    if m1 == "MG":
        print(DataStorageForElements.element_weight_list[11])
    if m1 == "AL":
        print(DataStorageForElements.element_weight_list[12])
    if m1 == "SI":
        print(DataStorageForElements.element_weight_list[13])
    if m1 == "P":
        print(DataStorageForElements.element_weight_list[14])
    if m1 == "S":
        print(DataStorageForElements.element_weight_list[15])
    if m1 == "CL":
        print(DataStorageForElements.element_weight_list[16])
    if m1 == "AR":
        print(DataStorageForElements.element_weight_list[17])
    if m1 == "K":
        print(DataStorageForElements.element_weight_list[18])
    if m1 == "CA":
        print(DataStorageForElements.element_weight_list[19])
    if m1 == "SC":
        print(DataStorageForElements.element_weight_list[20])
    if m1 == "TI":
        print(DataStorageForElements.element_weight_list[21])
    if m1 == "V":
        print(DataStorageForElements.element_weight_list[22])
    if m1 == "CR":
        print(DataStorageForElements.element_weight_list[23])
    if m1 == "MN":
        print(DataStorageForElements.element_weight_list[24])
    if m1 == "FE":
        print(DataStorageForElements.element_weight_list[25])
    if m1 == "CO":
        print(DataStorageForElements.element_weight_list[26])
    if m1 == "NI":
        print(DataStorageForElements.element_weight_list[27])
    if m1 == "CU":
        print(DataStorageForElements.element_weight_list[28])
    if m1 == "ZN":
        print(DataStorageForElements.element_weight_list[29])
    if m1 == "GA":
        print(DataStorageForElements.element_weight_list[30])
    if m1 == "GE":
        print(DataStorageForElements.element_weight_list[31])
    if m1 == "AS":
        print(DataStorageForElements.element_weight_list[32])
    if m1 == "SE":
        print(DataStorageForElements.element_weight_list[33])
    if m1 == "BR":
        print(DataStorageForElements.element_weight_list[34])
    if m1 == "KR":
        print(DataStorageForElements.element_weight_list[35])
    if m1 == "RB":
        print(DataStorageForElements.element_weight_list[36])
    if m1 == "SR":
        print(DataStorageForElements.element_weight_list[37])
    if m1 == "Y":
        print(DataStorageForElements.element_weight_list[38])
    if m1 == "ZR":
        print(DataStorageForElements.element_weight_list[39])
    if m1 == "NB":
        print(DataStorageForElements.element_weight_list[40])
    if m1 == "MO":
        print(DataStorageForElements.element_weight_list[41])
    if m1 == "TC":
        print(DataStorageForElements.element_weight_list[42])
    if m1 == "RU":
        print(DataStorageForElements.element_weight_list[43])
    if m1 == "RH":
        print(DataStorageForElements.element_weight_list[44])
    if m1 == "PD":
        print(DataStorageForElements.element_weight_list[45])
    if m1 == "AG":
        print(DataStorageForElements.element_weight_list[46])
    if m1 == "CD":
        print(DataStorageForElements.element_weight_list[47])
    if m1 == "IN":
        print(DataStorageForElements.element_weight_list[48])
    if m1 == "SN":
        print(DataStorageForElements.element_weight_list[49])
    if m1 == "SB":
        print(DataStorageForElements.element_weight_list[50])
    if m1 == "TE":
        print(DataStorageForElements.element_weight_list[51])
    if m1 == "I":
        print(DataStorageForElements.element_weight_list[52])
    if m1 == "XE":
        print(DataStorageForElements.element_weight_list[53])
    if m1 == "CS":
        print(DataStorageForElements.element_weight_list[54])
    if m1 == "BA":
        print(DataStorageForElements.element_weight_list[55])
    if m1 == "LA":
        print(DataStorageForElements.element_weight_list[56])
    if m1 == "CE":
        print(DataStorageForElements.element_weight_list[57])
    if m1 == "PR":
        print(DataStorageForElements.element_weight_list[58])
    if m1 == "ND":
        print(DataStorageForElements.element_weight_list[59])
    if m1 == "PM":
        print(DataStorageForElements.element_weight_list[60])
    if m1 == "SM":
        print(DataStorageForElements.element_weight_list[61])
    if m1 == "EU":
        print(DataStorageForElements.element_weight_list[62])
    if m1 == "GD":
        print(DataStorageForElements.element_weight_list[63])
    if m1 == "TB":
        print(DataStorageForElements.element_weight_list[64])
    if m1 == "DY":
        print(DataStorageForElements.element_weight_list[65])
    if m1 == "HO":
        print(DataStorageForElements.element_weight_list[66])
    if m1 == "ER":
        print(DataStorageForElements.element_weight_list[67])
    if m1 == "TM":
        print(DataStorageForElements.element_weight_list[68])
    if m1 == "YB":
        print(DataStorageForElements.element_weight_list[69])
    if m1 == "LU":
        print(DataStorageForElements.element_weight_list[70])
    if m1 == "HF":
        print(DataStorageForElements.element_weight_list[71])
    if m1 == "TA":
        print(DataStorageForElements.element_weight_list[72])
    if m1 == "W":
        print(DataStorageForElements.element_weight_list[73])
    if m1 == "RE":
        print(DataStorageForElements.element_weight_list[74])
    if m1 == "OS":
        print(DataStorageForElements.element_weight_list[75])
    if m1 == "IR":
        print(DataStorageForElements.element_weight_list[76])
    if m1 == "PT":
        print(DataStorageForElements.element_weight_list[77])
    if m1 == "AU":
        print(DataStorageForElements.element_weight_list[78])
    if m1 == "HG":
        print(DataStorageForElements.element_weight_list[79])
    if m1 == "TI":
        print(DataStorageForElements.element_weight_list[80])
    if m1 == "PB":
        print(DataStorageForElements.element_weight_list[81])
    if m1 == "BI":
        print(DataStorageForElements.element_weight_list[82])
    if m1 == "PO":
        print(DataStorageForElements.element_weight_list[83])
    if m1 == "AT":
        print(DataStorageForElements.element_weight_list[84])
    if m1 == "RN":
        print(DataStorageForElements.element_weight_list[85])

MolecularWeightGiver(Prefix_1)


    
