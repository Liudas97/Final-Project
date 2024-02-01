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

Throughout the analyzed period, five particular cars stood out and dominated the sport of Formula 1: Mercedes, Ferrari, McLaren Mercedes, Red Bull Racing Renault, Renault.

The analysis observed the Top 5 drivers' performances during over 58 or under 59 laps. Fernando Alonso, Max Verstappen, and Michael Schumacher have better performances driving over 58 laps. Lewis Hamilton and Sebastian Vettel have better performance driving under 59 laps.

Chart of top 5 winners victories over the 20 years shows, that there was a dominant period for a number of different people when they are able to win 10 or more competitions in a single year.
It is also appearent that these top 5 drivers are each others main competition, as usually two or three of the top 5 people have victories in the same year.
If this conclution is to be believed, then it is fair to say that Max Verstappen entered his dominant period in 2021 and he can be expected so stay in it for a few years to come.

Among all countries, that help F1 competions, only 4 countries are put to analysis, Great Britain, Hungary, Spain and Italy because they held competitions every year during the 20 years period. Comparing winning time, Italy has best (shortest) winning time results and the smallest spread of 8 minutes and it varies between 75 and 83 minutes. The biggest spread of 20 minutes in Hungary, meaning most unstable results, they vary between 95 and 117 minutes. All 4 countries show the longest winning times in years 2020, 2021 and 2022. 
