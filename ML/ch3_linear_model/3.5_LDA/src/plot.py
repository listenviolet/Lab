import numpy as np
import matplotlib.pyplot as plt 

f1 = plt.figure() 
#plt.axis([0, 4, 0, 10])

plt.plot([1,2,3], [1,2,3], 'go-', label='line 1', linewidth=2)
plt.plot([1,2,3], [1,4,9], 'rs-',  label='line 2')
plt.legend()
plt.show()