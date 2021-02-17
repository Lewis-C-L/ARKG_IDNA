#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 18:31:54 2021

@author: lewis
"""

import pandas as pd
import numpy as np

#importing data
df_IDNA = pd.read_csv('IDNA_holdings.csv', skiprows=9)
df_IDNA = df_IDNA.dropna()

df_ARKG = pd.read_csv('ARKG_holdings.csv')
df_ARKG = df_ARKG.dropna()



#tickers only as a list
IDNA_tickers = df_IDNA['Ticker'].tolist()
ARKG_tickers = df_ARKG['ticker'].tolist()

## common stocks ##
common_stocks = [x for x in IDNA_tickers if x in ARKG_tickers]


## unique stocks ##
# unique to IDNA
IDNA_unique = [x for x in IDNA_tickers if x not in ARKG_tickers]
# unique to ARKG
ARKG_unique = [x for x in ARKG_tickers if x not in IDNA_tickers]


## weighted similarity ##
#common stocks and weights
df_IDNA_common = df_IDNA.loc[df_IDNA['Ticker'].isin(common_stocks)][['Ticker', 'Weight (%)']]
df_ARKG_common = df_ARKG.loc[df_ARKG['ticker'].isin(common_stocks)][['ticker', 'weight(%)']]

#combine dataframes
df_compare = df_IDNA_common.set_index('Ticker').join(df_ARKG_common.set_index('ticker'))
#select minimum percetnage as a new column
df_compare['min'] = np.where(df_compare['Weight (%)']<=df_compare['weight(%)'],df_compare['Weight (%)'],df_compare['weight(%)'])

similarity_percentage = df_compare['min'].sum()
similarity_percentage = round(similarity_percentage,2)

print(similarity_percentage)


#Basic reasoning and example
# set1 = [A:0.25,b:0.5,c:0.05,d:0.2]     # note both sets sum to 1
# set2 = [A:0.5,b:0.25]

# 1 in 2 = 0.25 + 0.25 = 0.5
# 2 in 1 = 0.25 + 0.25 = 0.5

# method sum lowest value of common stocks.