import numpy as np
import matplotlib.pyplot as plt
import pandas

x = (1, 2, 3, 4, 5, 6, 7)
y = (5, 8, 3, 5, 7, 2, 9)

fontstyl = {'family':'serif','color':'blue','size':15}
fontttl = {'family': 'arial','color':'red','size':15}
#plt.plot( y, color='b', linestyle='--')
#plt.scatter( x, y, color='b', marker='^')
plt.bar( x, y, color='c', label='neat bars')

plt.xlabel("x-axis", fontdict=fontstyl)
plt.ylabel("y-axis", fontdict=fontstyl)

plt.title("simple line graph\norigin", fontdict=fontttl)
plt.grid(y)
plt.legend() #when invoking legend you need a label when ploting.
plt.show()
