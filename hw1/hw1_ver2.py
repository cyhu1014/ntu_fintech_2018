#hw1 for fintech
#ohlc extraction
#didn't process the data
import numpy as np
import pandas as pd
import sys

table  = pd.read_csv(sys.argv[1],encoding="big5",header=None ,dtype =str )
#table  = pd.read_csv("Daily_2018_09_28.csv",encoding="big5" ,header=None)
'''
x = int (table[0][1])
year = x//10000
month =x//100%100
day   =x%100
deadline_day = [17,21,21,18,16,20,18,15,19,17,21,19]
if( day > deadline_day[month]):
    month+=1
if(month ==13):
    year+=1
    month =1
deadline = year*100+month
'''

deadline = 999999
start = 0
end = 0
start_flag = 0
for i in range (1,len(table)):
    #print(i,table[2][i][6],"\"")
    if (table[1][i][0]=="T" and table[1][i][1]=="X" ):
        deadline = int(table[2][i])
        break
        if(start_flag == 0):
            start = i
            start_flag = 1
        if(table[2][i][6]=="/"):
            continue
        if(int(table[2][i]) < deadline):
            deadline = int(table[2][i])
            break
    #elif (start_flag == 1):
        #end = i
        #break

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

for i in range (start,len(table)):
    if (table[1][i][0]=="T" and table[1][i][1]=="X" ):
        if(table[2][i][6]=='/'):
            continue
        if(int(table[2][i])==deadline  ):     
            if(int(table[3][i]) >= open_time and int(table[3][i]) <= close  ):
                temp3i =int(table[3][i])
                temp4i = int (table[4][i])
                if (temp3i<open_temp):
                    open_temp  = temp3i
                    open_value = temp4i
                if (temp3i>=close_temp):
                    close_temp  = temp3i
                    close_value = temp4i
                if (temp4i>max_value ):
                    max_value = temp4i
                if (temp4i<min_value ):
                    #print(table_tx[i][3],table_tx[i][4])
                    min_value = temp4i
open_value = int(open_value)
max_value  = int(max_value)
min_value  = int(min_value)
close_value = int(close_value)
print(open_value,max_value,min_value,close_value)

