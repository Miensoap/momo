import pandas as pd
# df = pd.DataFrame({'KOSPI' : [1915,1961,2026,2567,2041],
# 'KOSDAQ' : [542,682,631,798,675]},
# index=[2014,2015,2016,2017,2018])
# print(df)
# print(df.describe())
# print(df.info())
from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()

sec = pdr.get_data_yahoo('005930.KS', start='2018-05-04')
msft = pdr.get_data_yahoo('MSFT', start='2018-05-04')
# print(sec.head(10))

tmp_msft = msft.drop(columns='Volume')
# print(tmp_msft.tail())

import matplotlib.pyplot as plt

# plt.plot(sec.index, sec.Close, 'b', label='Samsumg Electronics')
# plt.plot(msft.index, msft.Close, 'r--',label='Microsoft')
# # plt.show()
# plt.savefig('sam.png')

sec_dpc = (sec['Close']-sec['Close'].shift(1)) / sec['Close'].shift(1) * 100
sec_dpc.iloc[0]=0
plt.hist(sec_dpc, bins=18)
plt.grid(True)
plt.show()
plt.savefig('his.png')


