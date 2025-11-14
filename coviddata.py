import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sb


date = '05-26-2020'
path = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/05-26-2020.csv'

df = pd.read_csv(path)


date = datetime(year=2020, month=5, day=26)

date_string = date.strftime('%m-%d-%Y')


path = f'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/{date}.csv'

print(df.head)
df.info()
print("Coloumns before:")
print(df.columns.tolist())

to_drop = ['FIPS', 'Admin2', 'Province_State', 'Combined_Key', 'Last_Update']

df.drop(to_drop, inplace=True, axis=1)

print("Coloumns after:")
print(df.columns.tolist())

dfg = df.groupby('Country_Region')[['Confirmed', 'Deaths']].sum()

top_confirmed = dfg.sort_values(by='Confirmed', ascending=False).head(10)
top_deaths = dfg.sort_values(by='Deaths', ascending=False).head(10)

print("Top Confirmed: ")
print(top_confirmed)

print("Top Deaths: ")
print(top_deaths)

plt.figure(figsize=(10,5))
sb.barplot(data=top_confirmed.reset_index(), x='Country_Region', y='Confirmed')
plt.xlabel('Land')
plt.ylabel('Antal smittede')
plt.show()

plt.figure(figsize=(5,5))
plt.pie(
    top_confirmed['Deaths'], 
    labels=top_confirmed.index, 
)
plt.show()
