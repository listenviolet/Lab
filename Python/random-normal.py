import numpy as np

mu,sigma = 0, 0.1
s = np.random.normal(mu,sigma,15)
print(s)
print(np.mean(s))