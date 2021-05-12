import numpy
import random

#random亂數產生陣列
x = numpy.random.randint(1,150 , (2,3))
print(x)

#reshape調整形狀
#a = x.reshape(2,3)
#a.sort() #sort排序(小到大)將調整後的陣列由小排到大
#print(a)

fileName = "out2.npy"
with open(fileName , "wb") as fp:
    numpy.save(fp , x)