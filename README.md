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
Findings:



In the early and mid 2000 we can see that Michael Schumacher was the best. He only shows up in first 5 years of our sample data, but still is in the top 5 people with most wins over the 20years which shows his dominance.
Fernando Alonso is the driver that was the main competition for Schumacher and Alonso stayed relevant until 2014, however he is the only one in the list who didn't have his 'era'. He had consistent results over the years, getting few wins each year but never crossing a 10 win mark.
Next we have competition between 2 dominant contenders.
Lewis Hamilton and Sebastiam Vettel started winning within a year of each other.
Sebastian had a stronger start as he was winning more competitions from 2009 to 2014. This was his era.
Despite having a slower start than his rival, Lewis Hamilton got better over the years and was the most consistenmt.
His was the most dominant racer from 2014 to 2021, having 10 or more wins every year in this period of time, except for 9wins in 2017 and he is the record holder for most wins(103)
Since his first vicorty in 2007 he didn't have a single year with no wins, until 2022.
From the data we see, it's possible that 2021 might be the start of an era of Max Verstappen.
He got his first win in 2016 and won every year since then, 2021 being the most significant change as he won 10 wins, beating Lewis Hamilton who had 8.
2022 was another monumental year for Max, as he won 15 times, which is the most wins in a year from our sample data.
<img width="700" alt="Screenshot 2024-01-31" src="https://github.com/Liudas97/Final-Project/blob/main/Graphics/Change%20in%20wins%20over%20years.png?raw=true">
 
  
  
5. Created chart to observe differences in winning time over the year
<img width="700" alt="Screenshot 2024-01-31" src="https://github.com/Liudas97/Final-Project/blob/main/Graphics/Best%20times%20over%20years%20in%20top%204%20countries.png?raw=true">

## Conclusion

In conclusion, analysis of the Formula 1 Gran Prix over the past 20 years reveals some interesting patterns and trends in terms of winning drivers and cars. 

From analysis, we observe the top 5 cars that have dominated the sport during the analyzed period. In first place with 116 wins is Mercedes. Second is Ferrari with 83 wins. In third place with 48 wins is McLaren Mercedes car. Red Bull Racing Renault is in fourth place with 35 wins and in fifth place with 20 wins is Renault.

In Formula 1, the number of laps completed during a race can greatly impact a driver's performance and ultimately their chances of securing a victory. The second graph observes more specific results to understand how drivers fare based on the number of laps completed over 58 or under 59 laps. Fernando Alonso has better performance driving over 58 laps 17 > 15. Lewis Hamilton has better performance driving under 59 laps 46 < 57. Max Verstappen has better performance driving over 58 laps 19 > 16. Michael Schumacher has better performance driving over 58 laps 20 > 7. Sebastian Vettel has better performance driving under 59 laps 20 < 33.

Among all countries that hold F1 competions, only four countries are put to analysis - Great Britain, Hungary, Spain and Italy because they held competitions every year during the 20 years period. Comparing winning time, Italy has best (shortest) winning time results. Also Italy has the smallest spread of 8 minutes and it varies between 75 and 83 minutes. This means their results are most stable among compared countries. Spain and Hungary has  the longest winning times. The result might be influneced by number of laps or track difficulty. Also were noted biggest spread of 20 minutes in Hungary, meaning most unstable results, they vary between 95 and 117 minutes. Great Britain has spread of 15 minutes, between 80 and 95 (also noted the slowest time peak in 2014). It is explained by major car clash happened that year. Analyzing the trend of all 4 countries during 20 years period, all 4 countries show the longest winning times in years 2020, 2021 and 2022. Considering the fact, that it happened in a short period of time, still can not confirm that results are somehow connected or influnced by the same factor. Understanding the reasons might be a subject to separate analysis.
