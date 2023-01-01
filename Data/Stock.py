'''
@author: Erwin
@file: Stock.py
'''

from jqdatasdk import *
import pandas as pd

auth("17824852171", "Smile521")

# resample

# daily k -> weekly k
df = get_price('000001.XSHE',
               count=20,
               end_date='2022-12-31',
               frequency='daily',
               panel=False)
df['weekday'] = df.index.weekday

print(df)

df_week = pd.DataFrame()
df_week['open'] = df['open'].resample('W').first()
df_week['close'] = df['close'].resample('W').last()
df_week['high'] = df['high'].resample('W').max()
df_week['low'] = df['low'].resample('W').min()

print(df_week)

# sum
df_week['volume(sum)'] = df['volume'].resample('W').sum()
df_week['money(sum)'] = df['money'].resample('W').sum()

print(df_week)
