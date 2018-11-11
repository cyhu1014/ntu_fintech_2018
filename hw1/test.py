import numpy as np
import pandas as pd;
import string;
import sys;
 
DataFile=sys.argv[1];
#DataFile='/Users/mhci430/Downloads/Fintech_Data/Daily_2018_08_31.csv'
Data=pd.read_csv(DataFile ,encoding="big5" , dtype={'成交日期':str,'商品代號':str,'到期月份(週別)':str,'成交時間':int,'成交價格' :float})
 
 
#TX_index=np.zeros((len(Data)),dtype=bool)
#for i in range(len(Data)):
#    TX_index[i]='TX' in Data['商品代號'].values[i]
#
 
 
TX_Data=Data[Data['商品代號'].values=='TX     ']
#TX_Data=Data[TX_index]
D=np.unique(TX_Data['到期月份(週別)'].values)
NearFuture=D[0]
MinFloatS=99999999999;
for i in range(len(D)):
    s=D[i]
    result1 = ('/'in s)
    result2=('W' in s)
    if result1==False:
        if result2==True:
            floatS=float(s[:6])
        else:
            floatS=float(s)
        if(floatS<MinFloatS):
            MinFloatS=floatS
            NearFuture=D[i]
 
 
#TX_Data_Near_InTime=TX_Data[(TX_Data['到期月份(週別)'] == NearFuture)&(TX_Data['成交時間']>=84500)&(TX_Data['成交時間']<=134500)]
TX_Data_Near=TX_Data[(TX_Data['到期月份(週別)'] == NearFuture)]
TX_Data_Near_InTime_1=TX_Data_Near[TX_Data_Near['成交時間']>=84500]
TX_Data_Near_InTime=TX_Data_Near_InTime_1[TX_Data_Near_InTime_1['成交時間']<=134500]
 
 
TX_Data_Near_InTime_Open=TX_Data_Near_InTime[TX_Data_Near_InTime['成交時間'].values==TX_Data_Near_InTime['成交時間'].values.min()].head(1)
TX_Data_Near_InTime_Close=TX_Data_Near_InTime[TX_Data_Near_InTime['成交時間'].values==TX_Data_Near_InTime['成交時間'].values.max()].tail(1)
 
OpenPrice=int(TX_Data_Near_InTime_Open['成交價格'].values[0])
ClosePrice=int(TX_Data_Near_InTime_Close['成交價格'].values[0])
LowestPrice=int(TX_Data_Near_InTime['成交價格'].values.min())
HighestPrice=int(TX_Data_Near_InTime['成交價格'].values.max())
 
print(OpenPrice, HighestPrice, LowestPrice,ClosePrice)