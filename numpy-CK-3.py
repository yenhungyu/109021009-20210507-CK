#numpy save存檔
import numpy

fileName = "out2.npy"
with open(fileName , "wb") as fp:
    numpy.save(fp , 前面設置的代號)