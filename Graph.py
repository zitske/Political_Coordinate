from matplotlib import pyplot as plt
import matplotlib.patches as mpatches
from numpy.random import randn
import math

plt.hlines(y=0, xmin=-100, xmax=100)
plt.vlines(x=0, ymin=-100, ymax=100)
plt.xlabel('LIBERALISMO') 
plt.ylabel('ESQUERDA')


usrX = 25
usrY = -25
plt.plot(usrX, usrY,marker='o', markerfacecolor='black', markersize=5) 
userpoint = [usrX,usrY] 

#bolsonaro point
x = [85] 
y = [60] 
plt.plot(x, y,marker='o', markerfacecolor='yellow', markersize=10) 
#lula point
x2 = [-40] 
y2 = [20] 
plt.plot(x2, y2,marker='o', markerfacecolor='red', markersize=10) 
#ciro point
x3 = [-65] 
y3 = [50] 
plt.plot(x3, y3,marker='o', markerfacecolor='purple', markersize=10)
#marina point
x4 = [-20] 
y4 = [-30] 
plt.plot(x4, y4,marker='o', markerfacecolor='green', markersize=10)
#geraldo point
x5 = [10] 
y5 = [-70] 
plt.plot(x5, y5,marker='o', markerfacecolor='blue', markersize=10)  

data = [[85, 60], [-40, 20], [-65, 50], [-20,-30], [10,-70]] 
data.sort(key=lambda x: math.sqrt((float(x[0]) - (usrX)) ** 2 +
                                  (float(x[1]) - (usrY)) ** 2))

def resultante():
    if (data[:1] == [[85, 60]]):
        plt.title("Você se parece mais com o Bolsonaro")
    elif (data[:1] == [[-40, 20]]):
        plt.title("Você se parece mais com o Lula")     
    elif (data[:1] == [[-65, 50]]):
        plt.title("Você se parece mais com o Ciro Gomes") 
    elif (data[:1] == [[-20,-30]]):
        plt.title("Você se parece mais com a Marina Silva") 
    elif (data[:1] == [[10,-70]]):
        plt.title("Você se parece mais com o Geraldo Alckmin") 

resultante()
plt.grid()
plt.show()