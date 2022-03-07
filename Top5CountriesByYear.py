import pandas as pd
import numpy as np
import os

first_year = 1975
end_year   = 2021
years = end_year - first_year

number_of_importers = 30

input_path = "FilterDataSet.csv"
input_path = os.path.join( os.path.curdir , input_path )

data = pd.read_csv(input_path)
print(data,"\n\n\n")

ByImporterTotal = pd.read_csv(os.path.join( os.path.curdir , "ByImportTotal.csv" ))
ByImporterTotal.ix[:, ByImporterTotal.max().sort_values(ascending=False).index] #Sort
print(ByImporterTotal,"\n\n\n")

Count = np.empty( (number_of_importers,years+1) ,dtype=int)
i=0
for importer in list(ByImporterTotal.columns.values)[:number_of_importers]:
    j=0
    for year in range(first_year,end_year+1):
        Count[i,j] = np.int(np.sum(data.query(f"Importer == '{importer}' & Year == '{year}'")['Quantity']))
        j += 1
    i += 1

Top5countries = pd.DataFrame(data=Count ,
    index   = list(ByImporterTotal.columns.values)[:number_of_importers],
    columns = np.arange(first_year,end_year+1)
)

print(Top5countries,"\n\n\n")

Top5countries.to_csv( os.path.join( os.path.curdir, f"Top{number_of_importers}CountriesByYear.csv" ) )
