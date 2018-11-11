import numpy as np
def myStrategy(pastData, currPrice,i,j):
    action=0
    data_num = i
    data_num_2 = j
    data_num_3 = 5
    if(len(pastData)==0):
        return 0
    ##if datanum too small 
    if(len(pastData)<data_num):
        data_num=len(pastData) 
    if(len(pastData)<data_num_2):
        data_num_2=len(pastData)
    if(len(pastData)<data_num_3):
        data_num_3=len(pastData)

    if(data_num==data_num_2):
        return 0

    ma10 = np.mean(pastData[-data_num:])
    ma5 = np.mean(pastData[-data_num_2:])
    tendaysup = 1
    tendaysdown = 1
    for i in range (len(pastData)-1-data_num_3,len(pastData)-1):
        if(pastData[i]>pastData[i+1]):
            tendaysup = 0
            break
    for i in range (len(pastData)-1-data_num_3,len(pastData)-1):
        if(pastData[i]<pastData[i+1]):
            tendaysdown = 0
            break
    if(tendaysdown == 1 and ma10 > ma5):
        action = 1
    elif (tendaysup == 0 and tendaysdown == 0):
        action = 0
    elif(tendaysup == 1):
        action = -1

    
    
    ##print(len(pastData),ma5,ma10,action,tendaysup ,tendaysdown)
    
    
    return action
