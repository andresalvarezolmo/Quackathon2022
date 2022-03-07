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
head = ''
for importer in Importer:
    head = head + f',{importer}'
head = head + "\n"
print("[INFO] Computing and writng out\n")
with open( os.path.join( os.path.curdir , "ByImport.csv" ) ,"w" ) as outFile:
    outFile.write( head )
    i=1 #keep track of current genus
    for genus in data['Genus'].unique():
        print(f"[INFO] Current genus number {i}: {genus}")
        outFile.write(f"{genus}")
        j=1
        for importer in Importer:
            count = np.round(np.sum( data.query(f"Importer == '{importer}' & Genus=='{genus}'")['Quantity'] ))
            outFile.write(f",{int(count):d}")
            print(f"\t{j:3d}  {importer}")
            j += 1
        outFile.write("\n")
        i += 1

print("\n\n[INFO] Finished")