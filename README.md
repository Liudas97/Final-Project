# FINAL PROJECT
## Details
**Created by: [Liudas Dimša](https://github.com/Liudas97), [Agnė Koroliova](https://github.com/AgneKor) and [Danutė Glaveckaitė](https://github.com/NU-dot)**

This is the end project in Vilnius Coding School

Project theme: F1 Grand Prix winners analysis

The main goal of the project is to analyze different statistics of F1 Grand Prix winners over 20 year period (2003 - 2022)

In this project, we worked with Python language, CSV files

## Applied knowledge:

Used libraries: Pandas, MatplotLib

### data_scrapeF1.py

Used imports: BeautifulSoup, requests, pandas

Steps:

1. Getting data from URL (https://www.formula1.com/en/results.html) 
2. Getting needed data from URL as a table using Beautiful Soup and indicate analysis method (html.parser)
3. Clean up the data using "if" and "for" 
4. Exported data to the table in DataFrame format


### f1analysis.py

This is the main project file where all analyses were made. 

Steps:

1. Calculated total wins by car and created a graph of the Top 5 cars
<img width="700" alt="Screenshot 2024-01-31" src="https://github.com/Liudas97/Final-Project/blob/main/Graphics/wins%20by%20car%20top%205.png?raw=true">

2. Calculated total winners and created a graph of the Top 5 winners
<img width="700" alt="Screenshot 2024-01-31" src="https://github.com/Liudas97/Final-Project/blob/main/Graphics/wins%20by%20top%205%20winners.png?raw=true">

3.
<img width="700" alt="Screenshot 2024-01-31" src="https://github.com/Liudas97/Final-Project/blob/main/Graphics/Change%20in%20wins%20over%20years.png?raw=true">

4.
<img width="700" alt="Screenshot 2024-01-31" src="https://github.com/Liudas97/Final-Project/blob/main/Graphics/Best%20times%20over%20years%20in%20top%204%20countries.png?raw=true">

## Conclusion
