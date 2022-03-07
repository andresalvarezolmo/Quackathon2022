import pandas as pd
import numpy as np
import os

input_path = "ByYear.csv"
input_path = os.path.join( os.path.curdir , input_path )

output_path = "ByYearCumulative.csv"
output_path = os.path.join( os.path.curdir , output_path )

print("[INFO] Creating file and starting analysis\n")
with open(input_path , 'r') as ifile:
    with open(output_path , 'w') as ofile:
        ofile.write(ifile.readline())

        line = ifile.readline()
        while line != "":
            line = line.split(",")
            print(f"[INFO] Genus: {line[0]}")

            ofile.write(f"{line[0]}")
            cumulative = 0
            for number in line[1:]:
                cumulative += int(number)
                ofile.write(f",{cumulative:d}")
            
            ofile.write("\n")
            line = ifile.readline()

print("\n[INFO] Finsihed")