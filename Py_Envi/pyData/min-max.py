""" Find the normlaiztion value of a dataset"""
list1 = [16, 24, 28, 35, 40, 49, 61, 73, 87,92]

#find the min and max value 
min = min(list1)
max = max(list1)

# Iterate through the Dataset and calculate the normalization
print ("min-max Normalize:")
for x in list1:
    print ( round((x-min) / (max-min), 2))

# import pandas as pd
import numpy as np
import scipy.stats as stats
a = np.array([16, 24, 28, 35, 40, 49, 61, 73, 87,92])
print (stats.zscore(a))
