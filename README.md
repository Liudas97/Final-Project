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

2. Calculated total wins by winners and created a graph of the Top 5 winners
<img width="700" alt="Screenshot 2024-01-31" src="https://github.com/Liudas97/Final-Project/blob/main/Graphics/wins%20by%20top%205%20winners.png?raw=true">

3. Created chart to observe victories over the years of Top 5 winners 
<img width="700" alt="Screenshot 2024-01-31" src="https://github.com/Liudas97/Final-Project/blob/main/Graphics/Change%20in%20wins%20over%20years.png?raw=true">

4. Created chart to observe differences in winning time over the year
<img width="700" alt="Screenshot 2024-01-31" src="https://github.com/Liudas97/Final-Project/blob/main/Graphics/Best%20times%20over%20years%20in%20top%204%20countries.png?raw=true">

## Conclusion

In conclusion, analysis of the Formula 1 Gran Prix over the past 20 years reveals some interesting patterns and trends in terms of winning drivers and cars. 

From analysis, we observe the top 5 cars that have dominated the sport during the analyzed period. In first place with 116 wins is Mercedes. Second is Ferrari with 83 wins. In third place with 48 wins is McLaren Mercedes car. Red Bull Racing Renault is in fourth place with 35 wins and in fifth place with 20 wins is Renault.

In Formula 1, the number of laps completed during a race can greatly impact a driver's performance and ultimately their chances of securing a victory. The second graph observes more specific results to understand how drivers fare based on the number of laps completed over 58 or under 59 laps. Fernando Alonso has better performance driving over 58 laps 17 > 15. Lewis Hamilton has better performance driving under 59 laps 46 < 57. Max Verstappen has better performance driving over 58 laps 19 > 16. Michael Schumacher has better performance driving over 58 laps 20 > 7. Sebastian Vettel has better performance driving under 59 laps 20 < 33.

In the presented graphics (No 4)  we analyze 4 countries, Great Britain, Hungary, Spain and Italy bacause countries held competitions every year during the 20 years period. Comparing data we obtain, that Italy has best (shortest) winning time results. Also Italy has the smallest spread of results 8 minutes and it varies between 75 and 83 minutes. This means their results are most stable among compared countries. Spain and Hungary has  the longest winning times. The result might be influneced by number of laps or track difficulty. Also were noted biggest spread of 20 minutes  in Hungary,  meaning most unstable results, they vary between 95 and 117 minutes. Great Britain has spread of 15 minutes, between 80 and 95 (also noted the slowest time peak in 2014). It is explained by major car clash happened that year. Analyzing the trend of all 4 countries during 20 years period, were noted that all 4 countries show the longest winning times in years 2020, 2021 and 2022. Considering the fact, that it happened in a short period of time, still can not confirm that results are somehow connected or influnced by the same factor. Understanding of the reasons might be a subject to separate analysis.


