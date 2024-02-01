from numpy import array

a = (0, 1, 1, 1, 1, 0, 1)
b = (0, 0, 1, 1, 1, 0, 0)
match = False

if (len(a) == len(b)):
    match = True
    dim = len(a)
else:
    print("Dimension does Not matche !!!")

dotValue = 0
i = 0
while (match and i < dim):
    x1 = a[i]
    x2 = b[i]
    dotValue = dotValue + abs(x2*x1)
    print ("dotValue in loop", dotValue)
    i = i + 1

print ("dotValue total: ", dotValue)