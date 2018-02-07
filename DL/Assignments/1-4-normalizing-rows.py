import numpy as np 

def normalizeRows(x):
	x_norm = np.linalg.norm(x, axis = 1, keepdims = True)
	print(x_norm)
	x = x / x_norm
	return x

x = np.array([
    [0, 3, 4],
    [1, 6, 4]])
print("normalizeRows(x) = " + str(normalizeRows(x)))