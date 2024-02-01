import numpy as np
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.spatial.distance import squareform
import matplotlib.pyplot as plt


A = [0.000,0.330,0.309,0.826,0.266,0.102]
B = [0.330,0.000,0.007,0.382,0.289,0.161]
C = [0.309,0.007,0.000,0.871,0.804,0.187]
D = [0.826,0.382,0.871,0.000,0.812,0.480]
E = [0.266,0.289,0.804,0.812,0.000,0.957]
F = [0.102,0.161,0.187,0.480,0.957,0.000]

 
# mat = np.array([[0.0, 2.0, 0.1], [2.0, 0.0, 2.0], [0.1, 2.0, 0.0]]) TQ_2024-01/29 

mat = np.array([A, B, C, D, E, F])

dists = squareform(mat)

linkage_matrix = linkage(dists, "complete")

dendrogram(linkage_matrix, labels=["A", "B", "C", "D", "E", "F"])

plt.title("test")

plt.show()

 