# Find the top 15 species traded

# Note: I usually refer to animals for easier undertanding but not only animals are considered

################################################################
## IMPORTS

import os #for cross platform management of paths
import numpy as np

################################################################
## MAIN VARs

path_name = r"Trade_database_download_v2021.1" #Name of the folder containing the database files
path_name = os.path.join( os.path.curdir , path_name ) #Path to the folder.
delimiter = "," #delimiter used in csv

number_of_files = 46 #number of .csv in the database
number_of_anmials_to_choose = 15 #number of top ocurrance animals to chose

genusSet = {} # animals name tag # key: genus, value: number of them traded #initialize

################################################################
## LET'S ROCK

###################
## Counting

#Run though files
for i in range(1,number_of_files+1):

    print(f"[INFO] File number {i}")

    with open( os.path.join(path_name , f"trade_db_{i}.csv" ) ,'r' ) as file: #open file #filenames structure implied here!

        file.readline() #skip first row: header
        
        #Run through lines
        line = file.readline() #iteration 0
        while line != "":
            
            line = line.split(delimiter) #generate a list with columns in that row
            genus = eval(line[7]) #Column 7 cointains the genus #Eval to clean the string

            #Check if seen already
            if genus in genusSet:
                genusSet[genus] = genusSet[genus] + eval(line[9]) #Column 9 contains the number traded in that transaction
            else:
                genusSet.update({genus : eval(line[9])}) #Column 9 contains the number traded in that transaction
            

            #next iteration
            line = file.readline()

###################
## Choosing maxima

print("\n\n[INFO] Conting done, entering sorting")

#Transform dictionary with counting into list for easier processing.
genusNames = list(genusSet.keys())
genusCount = np.empty((len(genusNames)),dtype=int) #Alloc mem for counter

i = 0
for name in genusNames:
    genusCount[i]=genusSet[name]
    i += 1

#Sort by ocurrence
indices_of_maximun = np.argsort(genusCount)


##########################
## Saving 

print("[INFO] Sorting done, starting writing out")

# Printout to console
print("Chosen animals are:")
for index in indices_of_maximun[-number_of_anmials_to_choose:]:
    print(genusNames[index],"  ",genusCount[index])

# Save to file only chossing animals
with open( os.path.join( os.path.curdir , "ChosenAnimals.csv" ) ,"w" ) as file:
    for index in indices_of_maximun[-number_of_anmials_to_choose:]:
        file.write( f"{genusNames[index]}{delimiter}{genusCount[index]}\n" )

# Save to file the whole processing
with open( os.path.join( os.path.curdir , "Counting.csv" ) ,"w" ) as file:
    file.write(f"genus{delimiter}Count")
    for index in indices_of_maximun:
        file.write( f"{genusNames[index]}{delimiter}{genusCount[index]}\n" )