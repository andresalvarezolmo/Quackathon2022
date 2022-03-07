from ast import Import
import pandas as pd
import numpy as np
import os

input_path = "FilterDataSet.csv"
input_path = os.path.join( os.path.curdir , input_path )

data = pd.read_csv(input_path)
print(data,"\n\n\n")

print("[INFO] Gathering different importers")
Importer = data['Importer'].unique()

print("[INFO] Creating file and header")
head = f'{Importer[0]}'
for importer in Importer[1:]:
    head = head + f',{importer}'
head = head + "\n"
print("[INFO] Computing and writng out\n")
with open( os.path.join( os.path.curdir , "ByImportTotal.csv" ) ,"w" ) as outFile:
    outFile.write( head )
    j=1
    count = np.round(np.sum( data.query(f"Importer == '{Importer[0]}'")['Quantity'] ))
    outFile.write(f"{int(count):d}")
    print(f"\t{j:3d}  {Importer[0]}")
    for importer in Importer[1:]:
        count = np.round(np.sum( data.query(f"Importer == '{importer}'")['Quantity'] ))
        outFile.write(f",{int(count):d}")
        print(f"\t{j:3d}  {importer}")
        j += 1
    outFile.write("\n")

print("\n\n[INFO] Finished")