import pandas as pd
import numpy as np
import os

input_path = "FilterDataSet.csv"
input_path = os.path.join( os.path.curdir , input_path )

first_year = 1975
end_year   = 2021

data = pd.read_csv(input_path)
print(data,"\n\n\n")

head = ''
for year in range(first_year,end_year+1):
    head = head + f',{year}'
head = head + "\n"
with open( os.path.join( os.path.curdir , "ByYear.csv" ) ,"w" ) as outFile:
    outFile.write( head )
    i=1 #keep track of current genus
    for genus in data['Genus'].unique():
        print(f"[INFO] Current genus number {i}: {genus}")
        outFile.write(f"{genus}")
        for year in range(first_year,end_year+1):
            count = np.round(np.sum( data.query(f"Year == {year} & Genus=='{genus}'")['Quantity'] ))
            outFile.write(f",{int(count):d}")
        outFile.write("\n")
        i += 1