#fintech hw1 ohlc extraction
import sys
import numpy as np
import pandas as pd
table  = pd.read_csv(sys.argv[1],encoding="big5" ,header=None)
# (open, high, low, close)

table_tx =[]
index=0
date = 20181001
for i in range (1,len(table)):

    if (table[1][i][0]=="T" and table[1][i][1]=="X" ):
        table_tx.append([])
        table_tx[index].append(table[0][i])
        table_tx[index].append(table[1][i])
        table_tx[index].append(table[2][i])
        table_tx[index].append(table[3][i])
        table_tx[index].append(table[4][i])
        index+=1

df =pd.DataFrame(table_tx)
#find open
open_time =84500
close =134500
open_temp = 140000
open_value =0
for i in range (0,len(table_tx)):
    if(int(table_tx[i][0])==date):     
        if(int(table_tx[i][3]) >= open_time and int(table_tx[i][3]) <= close and int(table_tx[i][4]) >0):
            if (int(table_tx[i][3])<open_temp):
                open_temp  = table_tx[i][3]
                open_value = table_tx[i][4]
#find close
close_value = 0
close_temp  = 70000
for i in range (0,len(table_tx)):
    if(int(table_tx[i][0])==date):     
        if(int(table_tx[i][3]) >= open_time and int(table_tx[i][3]) <= close and int(table_tx[i][4])>0 ):
            if (int(table_tx[i][3])>= close_temp):
                close_temp  = table_tx[i][3]
                close_value = table_tx[i][4]
#find high low
max_value = 0
min_value = 99999
for i in range (0,len(table_tx)):
    if(int(table_tx[i][0])==date):     
        if(int(table_tx[i][3]) >= open_time and int(table_tx[i][3]) <= close and int(table_tx[i][4])>0):
            if (int(table_tx[i][4])>max_value ):
                max_value = table_tx[i][4]
            if (int(table_tx[i][4])<min_value ):
                print(table_tx[i][3],table_tx[i][4])
                min_value = table_tx[i][4]
                
print(open_value,max_value,min_value,close_value)

        
'''
'''