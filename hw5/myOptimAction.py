##ntu introduction to fintech 2018 fall 
# hw5
#方法:動態規劃
#使用參數有 moneyhold stockhold moneyptr stockptr 等四個list 分別到目前時間點最大的錢量 或最大的持股數
##以及他們是從原本的持股來或是現金來的
## 假設初始金錢為10000

def myOptimAction(priceVec, transFeeRate):
	import numpy as np	
	c= 1-transFeeRate
	money = 100000
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

	pointstock=1
	for i in range (dataLen-1,-1,-1):
		if (pointstock==0 and moneyptr[i]==0):
			actionVec[i]=0
			pointstock=0
		elif( pointstock==0 and moneyptr[i]==1):
			actionVec[i]=-1
			pointstock=1
		elif (pointstock==1 and stockptr[i]==0):
			actionVec[i]=1
			pointstock=0
		else:
			actionVec[i]=0
			pointstock=1
	for i in range (dataLen-1,-1,-1):
		if(actionVec[i]==0):
			continue
		elif(actionVec[i]==-1):
			break
		else:
			actionVec[i]=-1
	return actionVec
