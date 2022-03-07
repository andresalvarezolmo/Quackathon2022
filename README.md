# Quackathon2022
## Web page and results
Please visit https://andresalvarezolmo.github.io/Quackathon2022

## Information provided by the hackathon organizer (BlackRock): 
"CITES is an international treaty organization tasked with monitoring, reporting, and providing recommendations on the international species trade. This dataset contains records on every international import and export. Example Project: Produce a visualisation tool or a Jupyter notebook and an analysis of the trade of protected species around the world."

### Actual project aims: 
Download the 23 million entry dataset with international trades, curate the data extracting the most relevant bits, and produce a website plotting relevant charts about the biggest importing countries and traded protected species.

## Code and data analysis
### Disclaimer
Please note that the code written was not meant to be the most efficient possible, just meant solve a titanic curation task in less than 24 hours. Performance is not important as files are meant to be executed only once.

### Cleaning the data base:
Remark: The dataBase is too big to be loaded into memory (due to RAM limitations on the laptop used). For that reason, the database is analysed line-by-line to be cleaned into a smaller file `FilterDataBase.py` that can be used later.

Firstly, download and uncompress the dataset (https://trade.cites.org/) into the working directory, keeping the files on a separate folder
Secondly, Run `Counter.py` to pre analayse the data. This will choose the top traded species.
Thirdly, Rune `Writer.py` that would efectively clean the dataset into a smaller `FilterDataSet.csv` (That file is provided compress in this repository).

### Querying the database
The cleaned dataBase `FilterDataSet.csv` is small enough to be directly and efficiently process by pandas. We wrote specific Python script that parsed the pre-processed database to obtain relevant information, e.g: countries top 5 importing countries `ByImport.py`.

#### Further Examples
The files `ByImport.py`, `ByImportTotal.py`, `Research.py`, `ByYear.py`, `ByYearCumulative.py`, `ByYearTotal.py` and `Top5CountriesByYear.py` are specific queries to `FilterDataSet.csv` that generate small associated `.csv` to be directly plotted on Tableau by another member of the Team.
