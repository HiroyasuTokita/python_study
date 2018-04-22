# coding:utf-8

import numpy as np
import matplotlib.pyplot as plt

# データ作成
x = np.arange(0,6,0.1)
y1 = np.sin(x)
y2 = np.cos(x)

# グラフを表示
plt.plot(x,y1, label="sin")
plt.plot(x,y2, linestyle="--" , label="cos")
plt.xlabel("X");
plt.ylabel("Y");
plt.title("sin & cos")
plt.legend();
plt.show()
