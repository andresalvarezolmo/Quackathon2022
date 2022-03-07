import pandas as pd
import numpy as np
import os

input_path = "FilterDataSet.csv"
input_path = os.path.join( os.path.curdir , input_path )

first_year = 1975
end_year   = 2021

data = pd.read_csv(input_path)
print(data,"\n\n\n")

head = f'{first_year}'
for year in range(first_year+1,end_year+1):
    head = head + f',{year}'
head = head + "\n"
with open( os.path.join( os.path.curdir , "ByYearTotal.csv" ) ,"w" ) as outFile:
    outFile.write( head )
    count = np.round(np.sum( data.query(f"Year == {first_year}")['Quantity'] ))
    outFile.write(f"{int(count):d}")
    for year in range(first_year+1,end_year+1):
        count = np.round(np.sum( data.query(f"Year == {year}")['Quantity'] ))
        outFile.write(f",{int(count):d}")