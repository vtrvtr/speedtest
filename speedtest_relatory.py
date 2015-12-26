import argparse
from pandas.tseries import offsets
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt

csv_location = 'E:\Code\\speedtest\speedtest_table.csv'

'''Prepare data'''
df = pd.read_csv(csv_location, index_col=0)
relevant_columns = ["Download speed", "Upload speed", "Ping"]
df['Date'] = pd.to_datetime(df['Date'])
df.name = 'Avg all time'



def summary_last_days(days):
    last_days = df[df['Date'] > dt.datetime.now() - dt.timedelta(days=days)]
    last_days.name = 'Avg Last {} days'.format(days)
    return last_days


def print_s(*categories):
    for category in categories:
        print(category.name)
        for relevant_column in relevant_columns:
            print('\t{}: {}'.format(relevant_column,category[relevant_column].mean()))

def main():
    print_s(df)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Prints a relatory based on the speedtest_table file")
    parser.add_argument('--intervals', '-i', type=int, nargs='+', help='interval of days since current date you want to show avgs')
    args = parser.parse_args()
    if args.intervals:
        for interval in args.intervals:
            print_s(summary_last_days(interval))
    else:
        main()
