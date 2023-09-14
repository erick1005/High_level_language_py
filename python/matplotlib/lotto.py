import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

book = pd.read_csv('D:\project\coding\source codes\High_level_languages\python\matplotlib\Book1.csv')


winning_nums = book.iloc[:, 1]
#winning_nums = [15 , 35 , 17 , 7 , 27 , 14, 7 , 34 , 15 , 16 , 32 , 8, 35 , 8 , 36 , 2 , 15 , 22, 11 , 3 , 30 , 29 , 34 , 37, 16 , 20 , 7 , 39 , 38 , 11]
#frequecy = [x for x in range(len(winning_nums))]

bins = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]

plt.hist(winning_nums, bins, histtype='bar', rwidth=0.9)

#plt.bar(frequecy,winning_nums, color='k', label='number frequency')

plt.legend()
plt.grid()
plt.title('lotto results')
plt.xlabel('winning numbers')
plt.ylabel('frequency')

plt.show()
#print(winning_nums)