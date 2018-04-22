# coding:utf-8
import numpy as np

def AND(x1,x2):
    w1, w2, theta = 0.5, 0.5 , -0.7
    x = np.array([x1,x2])
    w = np.array([w1,w2])
    b = theta
    tmp = np.sum(x * w) + b
    if tmp <= 0 :
        return 0
    else:
        return 1

print("AND(0,0):{0}".format(AND(0,0)))
print(AND(1,0))
print(AND(0,1))
print(AND(1,1))
