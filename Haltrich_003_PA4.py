"""
Lincoln Haltrich
15310
003
11-5-2019
"""

print(__doc__)
import pandas as pd

Bottles = {'Contents': ["GreenPlastic"]}

LightLiquids = {'Contents': ["CornOil"]}

HeavyLiquids = {'Contents': ["Soap"]}

BottleWaste = {'Contents': ["Plastic"]}

ChemicalWaste = {'Contents': ["Soap"]}

OilWaste = {'Contents': ["CornOil", "LightOil"]}

Companies = {'Companies': ["TrashCo", "TheDump", "GarbageRUs"],
             'Contents': [BottleWaste, OilWaste, ChemicalWaste],
             'Amount(lb)': [2950, 3820, 4230],
             'Where': ["Landfill", "Ocean", "Ocean"]}

EPA = {'ids': ["Plastic", "oil", "Chemicals"],
       'Bio-Degradeable': ["GreenPlastic", "CornOil", "Soap"],
       'Non-Bio-Degradeable': ["plastic", "LightOil", "AntiFreeze"],
       'Bio-Items': [Bottles, LightLiquids, HeavyLiquids]}

#I created eight dictionaries but only two of them will be used in the code while the rest are used as future variables so the code can match the contents between the EPA and the waste companies
TheList = pd.DataFrame(Companies)
print(TheList)
print(len(TheList))

Regulation = pd.DataFrame(EPA)
print(Regulation)
print(len(Regulation))

A = Regulation['Bio-Items'].tolist()
print(len(A))

B = TheList['Contents'].tolist()
print(len(B))

#I turned the main dictionaries into a list and printed them to the console to display the data, and so this can be used to help my code dicipher the waste contents with the EPAs regulations 
def EPAcheck (B):
    """
Function: EPAcheck
Arguments: 1
What it does: A function that checks through the list of presented waste and notifies if the haul is good or not to dispose of.
    """
    if B[1] != A[1]:
        print("Harmful Plastic! Non-Disposable")
    elif B[1] == A[1]:
        print("Disposable")
    elif B[2] != A[2]:
        print("Harmful Oil! Non-Disposable")
    elif B[2] == A[2]:
        print("Disposable")
    elif B[3] != A[3]:
        print("Harmful Chemical! Non-Disposable")
    elif B[3] == A[3]:
        print("Disposable")
        
#I made the function to check the list of the EPA and the waste companies list and since the waste company list is combined it checks each of the contents, but from that the code then checks each contents with the EPAs contents and if the waste companies waste does not match the EPAs it doesnt get disposed of and the process is decided by a text of "Harmful (waste)! Non-Disposable" and if the waste is the same as the EPAs regulations then it passes with a text displayed "Disposable" 
print(EPAcheck.__doc__)
print('TEST')
print(EPAcheck(B))