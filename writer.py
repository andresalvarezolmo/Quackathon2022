# Reduce DataSet to interested columns and species

# Note: I usually refer to animals for easier undertanding but not only animals are considered

################################################################
## IMPORTS

import os #for cross platform management of paths
import numpy as np #delimiter used in csv

################################################################
## MAIN VARs

path_name = r"Trade_database_download_v2021.1" #Name of the folder containing the database files
path_name = os.path.join( os.path.curdir , path_name )#Path to the folder.
delimiter = "," #delimiter used in csv

#Paths for output names can be found through the file

number_of_files = 46 #number of .csv in the database

#Load to memory the animals we are interesested in
animals = [] #list with those animals name
with open( os.path.join( os.path.curdir, "ChosenAnimals.csv" ) , "r") as file:
    line = file.readline()
    while line != "":
        line = line.split(delimiter)
        animals.append(line[0]) # first column contains the name of the specie
        line = file.readline()

################################################################
## LET'S ROCK

###################
## Counting

#Run though files
print(os.path.curdir)
with open( os.path.join( os.path.curdir, "FilterDataSet.csv" ) , "w") as output_file:
    output_file.write('Year,Genus,Quantity,Importer,Exporter\n') #Columns we are going to keep in filtered data set

    #Run throgh files
    for i in range(1,1+number_of_files):

        print(f"[INFO] File number {i}")

        with open( os.path.join(path_name , f"trade_db_{i}.csv" ) ,'r' ) as input_file:

            input_file.readline() #skip first row, header

            #Run through lines
            line = input_file.readline() #iteration 0
            while line != "":
                line_breakdown = line.split(delimiter)
                #Check if we are interested in that line
                if eval(line_breakdown[7]) in animals: #Column 7 is the name of the animal
                    #Only choose what we are interested in
                    line = line_breakdown[1]+delimiter+line_breakdown[7][1:-1]+delimiter+line_breakdown[9]+delimiter+line_breakdown[11][1:-1]+delimiter+line_breakdown[12][1:-1]+'\n'
                    # Columns are 1: Year, 7: Genus, 9: Quantity, 10:Importer, 11:Exporter
                    # The [1:-1] is included to remove the " in the database, cleaning up data.
                    output_file.write(line)
                
                #Next iteration
                line = input_file.readline()