from numpy import array
import numpy as np
import openpyxl



vector_v1 = array([0, 1, 1, 1, 1, 0, 1])   
vector_v2 = array([0, 0, 1, 1, 1, 0, 1])   

dotValue = np.dot(vector_v1, vector_v2)

print (" DOT value is : ", dotValue)