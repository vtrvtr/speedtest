from pandas.tseries import offsets
import pandas as pd
import matplotlib as mpl
import seaborn as sns
import datetime as dt

csv_location = 'E:\Code\\speedtest\speedtest_table.csv'


df = pd.read_csv(csv_location, index_col=0)
df['Date'] = pd.to_datetime(df['Date'])
df.name = 'Avg all time'
relevant_columns = ["Download speed", "Upload speed", "Ping"]

d_delta = 7
last_days = df[df['Date'] > dt.datetime.now() - dt.timedelta(days=d_delta)]
last_days.name = 'Avg Last {} days'.format(d_delta)

def summary(*categories):
    for category in categories:
        print(category.name)
        for relevant_column in relevant_columns:
            print('\t{}: {}'.format(relevant_column,category[relevant_column].mean()))

summary(last_days, df)

