import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def sinplot(flip=1): #自定义一个函数
	x = np.linspace(0,14,100) #0-14取100个点

	for i in range(1,7): #画了7条线
		plt.plot(x,np.sin(x + i *0.5) * (7 - i) * flip) #sin函数
	plt.show()

sinplot()