
# coding: utf-8

# Task 1.1. Given a sequence of n values x1, x2, ..., xn and a window size k>0, the k-th moving average of
# the given sequence is defined as follows:
# The moving average sequence has n-k+1 elements as shown below.
# The moving averages with k=4 of a ten-value sequence (n=10) is shown below
# i 1 2 3 4 5 6 7 8 9 10
# ===== == == == == == == == == == ==
# Input 10 20 30 40 50 60 70 80 90 100
# y1 25 = (10+20+30+40)/4
# y2 35 = (20+30+40+50)/4
# y3 45 = (30+40+50+60)/4
# y4 55 = (40+50+60+70)/4
# y5 65 = (50+60+70+80)/4
# y6 75 = (60+70+80+90)/4
# y7 85 = (70+80+90+100)/4
# 
# Thus, the moving average sequence has n-k+1=10-4+1=7 values.
# Problem Statement:
# Write a function to find moving average in an array over a window:
# Test it over [3, 5, 7, 2, 8, 10, 11, 65, 72, 81, 99, 100, 150] and window of 3.

# In[1]:


import numpy as np
from numpy import convolve
 
def movingaverage (values, window):          #function to calculate moving average in an array over a window
    weights = np.repeat(1.0, window)/window  #array([0.33333333, 0.33333333, 0.33333333])
    mov_avg_seq = np.convolve(values, weights, 'valid') #Returns the discrete, linear convolution of two one-dimensional sequences
    return mov_avg_seq

TestData = [3, 5, 7, 2, 8, 10, 11, 65, 72, 81, 99, 100, 150]
print("The moving average sequence has n-k+1 elements as shown below: 13-3+1 = 11 array elements")
print("The moving averages with k=3 of a thirtheen-value sequence (n=13) is shown below")
array = movingaverage(TestData,3)
print(array)


# Task 2.1. How-to-count-distance-to-the-previous-zero
# For each value, count the difference back to the previous zero (or the start of the Series,
# whichever is closer)
# create a new column 'Y'
# Consider a DataFrame df where there is an integer column 'X'
# import pandas as pd
# df = pd.DataFrame({'X': [7, 2, 0, 3, 4, 2, 5, 0, 3, 4]})

# In[2]:


import pandas as pd
df = pd.DataFrame({'X': [7, 2, 0, 3, 4, 2, 5, 0, 3, 4]}) 
#1:first finding out indices of zeros and adding first indices with -1: [-1,2,7]
izero = np.r_[-1, (df['X'] == 0).nonzero()[0]]  
#2:Creating array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
idx = np.arange(len(df))
#3:array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])-array([1, 2, 0, 1, 2, 3, 4, 0, 1, 2])
df['Y'] = idx - izero[np.searchsorted(izero - 1, idx) - 1]
print(df)


# Task 2.2. Create a DatetimeIndex that contains each business day of 2015 and use it to index a Series of
# random numbers.

# In[3]:


dti = pd.date_range(start='2015-01-01', end='2015-12-31', freq='B') #B business day frequency
s = pd.Series(np.random.rand(len(dti)), index=dti)                  #creating series for Random values in a given Datetimeindex
s


# Task 2.3. Find the sum of the values in s for every Wednesday

# In[4]:


print(s[s.index.weekday == 2].sum())     #The day of the week with Monday=0,Tuesday=1,Wednesday=2...Sunday=6
print(s[dti.weekday == 2].sum())         #The day of the week with Monday=0,Tuesday=1,Wednesday=2...Sunday=6


# Task 2.4. Average For each calendar month

# In[5]:


s.resample('M').mean()    #Convenience method for frequency conversion and resampling of time series


# Task 2.5 For each group of four consecutive calendar months in s, find the date on which the highest
# value occurred.

# In[6]:


s.groupby(pd.Grouper(freq='4M')).idxmax()

