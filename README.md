# **FORMULE 1** STATISTICAL ANALYSIS
## Details
**Created by: [Liudas Dimša](https://github.com), [Agne](https://github.com) and [Danute Glaveckaite](https://github.com/NU-dot)**

This is the end project in Vilnius Coding School

Project theme: Formule 1 statistical data analysis

The main goal of the project is to find out who have the best performance during 20 years period (2003 - 2023)

In this project we used to work with Python language, CSV files

## Applied knowledge:

Used libraries: Pandas, MatplotLib

### postgres.py
Used database adapter: main.py

### web_scrap.py
Used imports: BeautifulSoup, requests

Steps:

1. Getting data from URL (https://www.formula1.com/en/results.html) 
2. Getting needed data from url as table using Beautiful soup and indicate analysis method (html.parser)
3. Using "if" and "for" received data inserted into table in Postgres


### final_project.py

This is the main project file where all analysis were made. All visuals are controlled by functions, which helps to separate all graphs in the code.

Steps:

1. Unified all INDEXES data by formating Dates and selected 'Close' price columns

2. Calculations for each index:

3. Visualisation of calculations:

## Conclusion
