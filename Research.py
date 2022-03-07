import pandas as pd
import numpy as np
import os


path_name = r"Trade_database_download_v2021.1"
path_name = os.path.join( os.path.curdir , path_name )
delimiter = ","

number_of_files = 46

ByResearcher = { "T":[0] , "S":[0], "":[0] , "counter":[0] , "P":[0], "B":[0], "E":[0], "Z":[0],
 "G":[0], "H":[0], "L":[0], "M":[0], "N":[0], "Q":[0]}

#Run though files
for i in range(1,number_of_files+1):

    print(f"[INFO] File number {i}")

    with open( os.path.join(path_name , f"trade_db_{i}.csv" ) ,'r' ) as file:

        file.readline() #skip first row, header
        

        #Run through lines
        line = file.readline() #iteration 0
        while line != "":
            line = line.split(delimiter)
            quantity = eval(line[9])
            ByResearcher['counter'][0] += quantity
            purpose = eval(line[14])
            
            ByResearcher[purpose][0] += quantity
            line = file.readline()

ByResearcher = pd.DataFrame(ByResearcher)
ByResearcher.rename({"": "NA"})
ByResearcher.to_csv( os.path.join( os.path.curdir , "ByResearcher.csv" ) )