import numpy

numpy.zeros((2,3))#2*3全0的陣列
n = numpy.ones((2,3,4)) * 80#2*3*4全1的陣列
print(n)
numpy.arange((1,10,2))#從1開始不超過10間隔為2的均勻數值陣列
numpy.linspace(0.10,5)#從0到10均勻的5個數值陣列
numpy.full((3,2),8)#full填滿,全以8填滿的概念,上面的第4行的概念

a = numpy.array([1,2,3,4]) #一維陣列
#print(a)
b = numpy.array([(3,8,1.6,4) , (1,2,3,4)] , dtype = float) #二維陣列
#print(b)
c = numpy.array([[(4.5,3.5,1,3) , (1,2,3,4)] , [(3.6,2.5,1,3), (1,2,3,4)]] , dtype = float)#dtype=float小數點的需要
#三維陣列
#print(c)