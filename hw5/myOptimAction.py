##ntu introduction to fintech 2018 fall 
# hw5
#方法:動態規劃
#使用參數有 moneyhold stockhold moneyptr stockptr 等四個list 分別到目前時間點最大的錢量 或最大的持股數
##以及他們是從原本的持股來或是現金來的
## 假設初始金錢為10000

def myOptimAction(priceVec, transFeeRate):
	import numpy as np	
	c= 1-transFeeRate
	money = 10000
	dataLen = len(priceVec)
	actionVec = np.zeros(dataLen)
	moneyhold = []
	stockhold = []
	moneyptr  = [] #0 from money  ; 1 from stock
	stockptr  = []
	moneyhold.append(money)
	stockhold.append(money/priceVec[0]*c)
	moneyptr.append(0)
	stockptr.append(0)
	for i in range (1,dataLen):
        
		if(moneyhold[i-1]>stockhold[i-1]*priceVec[i]*c):
			moneyptr.append(0)
			moneyhold.append(moneyhold[i-1])
		else:
			moneyptr.append(1)
			moneyhold.append(stockhold[i-1]*priceVec[i]*c)
		
		if(stockhold[i-1]>moneyhold[i-1]/priceVec[i]*c):
			stockptr.append(1)
			stockhold.append(stockhold[i-1])
		else:
			stockptr.append(0)
			stockhold.append(moneyhold[i-1]/priceVec[i]*c)
		print(i,moneyhold[i],stockhold[i])
       

        
        
	key=2
	for i in range (dataLen-1,-1,-1):
		if (key==1 and moneyptr[i]==0):
			actionVec[i]=0
			key=1
		elif( key==1 and moneyptr[i]==1):
			actionVec[i]=-1
			key=2
		elif (key==2 and stockptr[i]==0):
			actionVec[i]=1
			key=1
		elif (key==2 and stockptr[i]==1):
			actionVec[i]=0
			key=2


	return actionVec
