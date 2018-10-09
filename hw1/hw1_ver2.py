#hw1 for fintech
#ohlc extraction
#didn't process the data
import numpy as np
import pandas as pd
import sys

table  = pd.read_csv(sys.argv[1],encoding="big5" ,header=None)
x = int (table[0][1])
year = x//10000
month =x//100%100
day   =x%100
deadline_day = [17,21,21,18,16,20,18,15,19,17,21,19]
'''
if( day > deadline_day[month]):
    month+=1
if(month ==13):
    year+=1
    month =1
deadline = year*100+month
'''
print(table[2][65535][6])
deadline = 999999
'''
for i in range (1,len(table)):
    print(i,table[2][i][6],"\"")
    if (table[1][i][0]=="T" and table[1][i][1]=="X" ):
        if(table[2][i][6]=="/"):
            continue
        if(int(table[2][i]) < deadline):
            deadline = int(table[2][i])
'''
#find open
open_time =84500
close =134500
open_temp = 140000
open_value =0
#find close
close_value = 0
close_temp  = 70000
#find high low
max_value = 0
min_value = 99999
for i in range (1,len(table)):
    if (table[1][i][0]=="T" and table[1][i][1]=="X" ):
        if(table[2][i][6]=='/'):
            continue
        if(int(table[2][i])==deadline  ):     
            if(int(table[3][i]) >= open_time and int(table[3][i]) <= close  ):
                if (int(table[3][i])<open_temp):
                    open_temp  = table[3][i]
                    open_value = table[4][i]
                if (int(table[3][i])>=close_temp):
                    close_temp  = table[3][i]
                    close_value = table[4][i]
                if (int(table[4][i])>max_value ):
                    max_value = table[4][i]
                if (int(table[4][i])<min_value ):
                    #print(table_tx[i][3],table_tx[i][4])
                    min_value = table[4][i]
open_value = int(open_value)
max_value  = int(max_value)
min_value  = int(min_value)
close_value = int(close_value)


print(open_value,max_value,min_value,close_value)

