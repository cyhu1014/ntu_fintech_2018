#introduction to fintech (2018,fall)
#final project
#implement a trading strategy for 台指期 

import pandas as pd
import numpy as np
import talib

def myStrategy(dailyOhlcvFile, minutelyOhlcvFile, openPrice):
    
    money_state = 1
    RSI_threshold=50
    open_of_daily = dailyOhlcvFile['open']
    SMA = talib.MA(open_of_daily,3)
    BMA = talib.MA(open_of_daily,120)
    RSI = talib.RSI(open_of_daily)
    length= len(SMA)-1
    if(SMA[length]>BMA[length] and RSI[length]>RSI_threshold ):
        return 1
    elif (SMA[length]<BMA[length] and RSI[length]<RSI_threshold ):
        return -1
    else:
        return 0

'''
minute_file = pd.read_csv("ohlcv_minutely.csv")
daily_file  = pd.read_csv("ohlcv_daily.csv")
open_of_daily = daily_file['open']
money = 1000000
stock = 0
state = 0
transaction_fee = 100
money_state = 1
for i in range (500, len(daily_file)-1):
    action = myStrategy (daily_file[:i-1], 0, open_of_daily[i])
    if(action == 1 and money_state==1):
        money = money-transaction_fee
        stock = money/open_of_daily[i]
        money = 0
        money_state = 0
    elif(action == -1 and money_state == 0):
        money = stock*open_of_daily[i]-transaction_fee
        stock = 0
        money_state = 1
money+=stock*open_of_daily[len(open_of_daily)-1]
print(money/1000000) '''  
