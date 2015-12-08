import speedtest_cli as st
from datetime import datetime
import pandas as pd
from collections import OrderedDict

csv_location = 'E:\Code\\speedtest\speedtest_table.csv'
current_date = datetime.now()

dspeed, upspeed, ping, server_info = st.speedtest()

raw_data = OrderedDict([('Date', [current_date]),
                        ('Download speed', [dspeed]),
                        ('Upload speed',  [upspeed]),
                        ('Ping', [ping]),
                        ('Server', [server_info['sponsor']]),
                        ('S latitude', [server_info['lat']]),
                        ('S longitude', [server_info['lon']]),
                        ('S id', [server_info['id']])])

columns = [k for k in raw_data.keys()]
df = pd.DataFrame(data=raw_data, columns=columns)
df.to_csv(csv_location, mode='a', ignore_index=True, header=False)
