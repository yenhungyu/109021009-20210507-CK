#課堂練習
#加密

import sys
import random
import numpy

data = list("This is book")

if __name__ == "__main__":
    if len(sys.argv) >2:
        seedValu = int(sys.argv[1])
        data = list(sys.argv[2])
        random.seed(seedValu)
        random.shuffle(data)
        print("".join(data))

#解密(回家作業(不太會寫....))

seedValu = int(sys.argv[1])
data = list(sys.argv[2])
random.shuffle(data)
for i in range(data):
    data = i%len(sys.argv)
    seedValu = i ^ data
    buff.append(i)
print(i)