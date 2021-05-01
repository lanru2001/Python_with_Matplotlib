#Using Matplotlib to plot quality graphs, charts and figures  in Python 
import matplotlib
import matplotlib.pyplot as plt 

x=[100,200,300,400,500,600,700]
y=[20,30,40,50,60,70,80]


plt.title("sales  data")
plt.xlabel("value of sales")
plt.ylabel("Number of sales ")
plt.scatter(x,y)
plt.show()
