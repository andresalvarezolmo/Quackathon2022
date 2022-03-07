# Quackathon2022
## Code and data analysis
### Disclaimer
Please note that the code writen coulb be very unefficient sometimes because devolping speed was the key point. Performance is not important as files are meant to be executed only once.

### Cleaning the data base:
Remark: The dataBase is too big to be loaded into memory (due to RAM limitations on the laptop used). For that reason, the database is analysed line-by-line to be cleaned into a smaller file `FilterDataBase.py` that can be used later.

Firstly, download and uncompress the dataset into the working directory, keeping the files on a separate folder.
Secondly, Run `Counter.py` to pre analayse the data. This will choose the top traded species.
Thirdly, Rune `Writer.py` that would efectively clean the dataset into a smaller `FilterDataSet.csv` (That file is provided compress in this repository).

### Making queries to the data base
The cleaned dataBase `FilterDataSet.csv` is small enogh to be directly and efficiently process by pandas.

The files `ByImport.py`, `ByImportTotal.py`, `Research.py`, `ByYear.py`, `ByYearCumulative.py`, `ByYearTotal.py` and `Top5CountriesByYear.py` are specific queries to `FilterDataSet.csv` that generate small associated `.csv` to be directly plotted on Tableu by another member of the Team.
