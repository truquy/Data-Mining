''' The norm of a vector refers to the length or magnitude
of its vector. norm is a measure of its distance from the 
origin in vector space. Donated as ||x||
    Using numpy or scipy library to perform the calculation'''

from numpy import array
from numpy.linalg import norm
from scipy.linalg import *


#insert vector
vector_V1 = array([0, 1, 1, 1, 1, 0, 1])

# Calculate the norm or norm_l1, norm_l2 using Numpy
norm_V1 = norm(vector_V1,1)
norm_V1_L2 = norm(vector_V1)

# Calculation using the Scipy
norm_V1_sci = norm(vector_V1,1)
norm_V1_L2_sci = norm(vector_V1)

# Print out the result
    # Numpy method
print ("Vector v1 value: ", vector_V1)
print ("Norm V1 numpy value: ", norm_V1)
print ("Norm_L2 V1 numpy value: ", norm_V1_L2)

    # Scipy method
print ("Norm V1 sci value: ", norm_V1)
print ("Norm_L2 V1 sci value: ", norm_V1_L2_sci)