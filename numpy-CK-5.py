#shuffle打亂

import numpy
import random

numpy.random.seed(5522)
x = numpy.random.randint(1,150,(2,3))
print(x)
y = x.reshape(1,6)
print(y)
z = numpy.random.shuffle(y)
print(z)

#加密
data = list("that is a dog")
print("".join(data))
#print(data)
random.seed(5522)
random.shuffle(data)
print("".join(data))
