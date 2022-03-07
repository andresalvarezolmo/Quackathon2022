#Dying
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os


Data = pd.read_csv(os.path.join( os.path.curdir , "Top30CountriesByYear.csv" ),index_col=0)
print(Data,"\n\n\n")

plt.figure()

for country in list(Data.index.values):
    plt.plot( Data.columns.values, Data.query(f"index == '{country}'").values[0] , label=country )

plt.xlabel("Year")
plt.ylabel("Imported")
plt.grid()
plt.legend()

plt.show()