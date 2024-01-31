from bs4 import BeautifulSoup
import requests
import pandas as pd

all_years_table = []

for i in range(2003, 2023):
    url=f"https://www.formula1.com/en/results.html/{i}/races.html"
    response=requests.get(url)
    # print(response.status_code)
    soup = BeautifulSoup(response.content, 'html.parser')
    F_1 = []
    table = soup.find('table')
    if table:
        rows = table.find_all('tr')
        for row in rows:
            cells = row.find_all('td')  # table data
            if len(cells) > 1:
                grand_prix = cells[1].text.strip()
                datos = cells[2].text.strip().replace(' ', '-')
                winner = cells[3].text.strip().replace('\n',' ')
                car = cells[4].text.strip()
                laps = cells[5].text.strip()
                time = cells[6].text.strip()

                F_1.append({
                    'Grand prix': grand_prix,
                    'Date': datos,
                    'Winner': winner,
                    'Car': car,
                    'Laps': laps,
                    'Best time': time
                })
        year_df = pd.DataFrame(F_1)
        year_df['Year'] = i
        all_years_table.append(year_df)
        df = pd.concat(all_years_table)
        # print(df)
df.to_csv('F1.csv', index=False)