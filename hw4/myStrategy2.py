'''
def myStrategy(pastData, currPrice):
    import numpy as np
    param=[0, 19]
    windowSize=296
    alpha=param[0]
    beta=param[1]
    action=0
    dataLen = len(pastData)
    if dataLen<windowSize:
        ma=np.mean(pastData)
        return 0
    windowedData=pastData[-windowSize:]
    ma=np.mean(windowedData)
    if (currPrice-alpha)>ma:
        action=1
    elif (currPrice+beta)<ma:
        action=-1
    else:
        action=0
    return action
'''
def create_MA (spy,days):
    MA = []
    means = 0
    idx = 'Adj Close'
    for i in range (days):
        means += spy[idx][i]
        temp_mean = means/(i+1)
        MA.append(temp_mean)
    for i in range (days,len(spy)):
        means += spy[idx][i]
        means -= spy[idx][i-days]
        temp_mean = means/days
        MA.append(temp_mean)

    return MA

def predict (money , ma_low ,ma_high,spy):
    idx = 'Adj Close'
    flag_buy = 1 
    hold = 0
    for i in range (len(spy)-1):
        if (ma_low[i] > ma_high[i] and flag_buy == 1 ):
            hold = money/spy[idx][i]
            money -= hold *spy[idx][i]
            flag_buy = 0
            #print("buy :" ,i)
        if (ma_low[i] < ma_high[i] and flag_buy == 0 ):
            money += hold*spy[idx][i]
            hold = 0
            flag_buy = 1
            #print("sale :" ,i)
    money+= hold * spy[idx][len(spy)-1]
    return money

def myStrategy(pastData, currPrice,low,high): #7,5 run to i =53
    
    ma_low = calculate_mean(pastData,low)
    ma_high = calculate_mean(pastData,high)
    action = 0
    if (ma_low>ma_high):
        action=1
    else:
        action=-1
    
    return action
    '''
    import numpy as np
    param=[0, 19]
    windowSize=296
    alpha=param[0]
    beta=param[1]
    action=0
    dataLen = len(pastData)
    if dataLen<windowSize:
        ma=np.mean(pastData)
        return 0
    windowedData=pastData[-windowSize:]
    ma=np.mean(windowedData)
    if (currPrice-alpha)>ma:
        action=1
    elif (currPrice+beta)<ma:
        action=-1
    else:
        action=0
    
    return action
    '''

def calculate_mean (pastData,days):
    
    data_num = len(pastData)
    if(data_num==0):
        return 0
    mean = 0
    if(data_num<days):
        for i in range (data_num):
            mean+=pastData[i]
        mean/=data_num
    else:
        for i in range (data_num-days,data_num):
            mean+=pastData[i]
        mean/=days
    return mean
