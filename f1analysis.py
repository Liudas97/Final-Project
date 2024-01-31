import pandas as pd
import matplotlib.pyplot as plt
pd.options.mode.chained_assignment = None


df = pd.read_csv('F1.csv')

# Removed initials from the end of the 'Winner'
df['Winner'] = df['Winner'].apply(lambda x: ' '.join(x.split()[:-1]))
# Changed format to Date:
df['Date'] = pd.to_datetime(df['Date'])
df['Date_Year']=df['Date'].dt.year
# Changed format to time:
df['Best time'] = df['Best time'].replace('55:30.622', '0:55:30.622')
df['Best time'] = pd.to_datetime(df['Best time'], format='%H:%M:%S.%f').dt.time

# Sorted total wins by driver:
winner_totals = df['Winner'].value_counts()
# Sorted Top 5 winners as index:
top_5_winners = winner_totals.head(5).index

# Count the wins for each of the top 5 winners in each year:
wins_over_years_top_5 = df[df['Winner'].isin(top_5_winners)].groupby(df['Date_Year'])['Winner'].value_counts().unstack().fillna(0)

# Calculated total wins by person('Winner')
top5_most_wins_by_driver = df['Winner'].value_counts().head(5)
# Calculated total wins by a car
top5_most_wins_by_car = df['Car'].value_counts().head(5)


#Find 2 types of victories, one where tracks are longer than 58 laps and another one where tracks are shorter than 59:
top5_winners_over_58_laps = df[df['Laps'] > 58]['Winner'].value_counts().head(5)
top5_winners_under_59_laps = (top5_most_wins_by_driver - top5_winners_over_58_laps)

top5_most_wins_by_driver = top5_most_wins_by_driver.sort_index()
top5_winners_over_58_laps = top5_winners_over_58_laps.sort_index()
top5_winners_under_59_laps = top5_winners_under_59_laps.sort_index()


# Top 5 most wins by car:
colours = ['dimgray', 'r', 'darkorange', 'b', 'gold']
plt.figure(figsize=(12, 8))
plt.bar(top5_most_wins_by_car.index, top5_most_wins_by_car.values, color=colours)
plt.xlabel('Car')
plt.ylabel('Total wins')
plt.title('Total wins by car', fontsize=20)
plt.xticks(rotation=0)
plt.show()

# Total wins by top5 winners:
x = top5_most_wins_by_driver.index
y1 = top5_winners_over_58_laps.values
y2 = top5_winners_under_59_laps.values

plt.figure(figsize=(12, 8))
plt.bar(x, y1, label='Tracks over 58 laps')
plt.bar(x, y2, bottom=y1, color='c', label='Tracks >= 58 laps')
plt.ylabel('Total wins')
plt.title('Total wins by Top5 winners', fontsize=20)
plt.xticks(rotation=0)
plt.legend()
plt.show()


# Top 5 drivers victories per year over the 20 years:
plt.figure(figsize=(12, 8))
for driver in wins_over_years_top_5.columns:
    plt.plot(wins_over_years_top_5.index, wins_over_years_top_5[driver], label=driver, linewidth=2)
plt.xlabel('Year')
plt.ylabel('Number of Wins')
plt.title('Change in number of wins over the 20 years (Top 5 winners)', fontsize=20)
plt.xticks(wins_over_years_top_5.index[::1])
plt.legend()
plt.show()


# Sorted total Grand prix by Country:
Grand_prix_totals = df['Grand prix'].value_counts()
# Sorted Top 4 Grand prix as index:
top_4_most_Grand_prix = Grand_prix_totals.head(4).index
# Count the Best time for each of the top 4 countries in each year:
winning_times_over_years_top_4 = df[df['Grand prix'].isin(top_4_most_Grand_prix)].groupby(df['Date_Year'])['Best time'].value_counts()
# Filter the df so that we only see the top 4 countries
df_top_4_countries = df[df['Grand prix'].isin(top_4_most_Grand_prix)]
# Changing Best time format to minutes for more convenient display:
df_top_4_countries['Best time'] = df_top_4_countries['Best time'].apply(lambda x: pd.to_timedelta(str(x)).total_seconds() / 60)


#Top 4 countries with most Grand prix held and their best_winning_time over 20 years:
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 8), sharex=True)
for i, country in enumerate(top_4_most_Grand_prix):
    ab = axes[i // 2, i % 2]
    country_data = df_top_4_countries[df_top_4_countries['Grand prix'] == country]
    ab.plot(country_data['Year'], country_data['Best time'], label=country)
    ab.set_title(country)
    ab.set_xlabel('Year')
    ab.set_ylabel('Best Time in minutes')
    ab.set_xticks(range(df_top_4_countries['Year'].min(), df_top_4_countries['Year'].max() + 1, 2))

plt.suptitle('Winning time over the years by country (Top 4 countries with most Grand prix held)', fontsize=20)
plt.tight_layout()
plt.show()