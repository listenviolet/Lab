import numpy as np 

x = np.array([
	[[ 0.67826139,  0.29380381], 
	[ 0.90714982,  0.52835647],
    [ 0.4215251 ,  0.45017551]],

   [[ 0.92814219,  0.96677647],
    [ 0.85304703,  0.52351845],
    [ 0.19981397,  0.27417313]],

   [[ 0.60659855,  0.00533165],
    [ 0.10820313,  0.49978937],
    [ 0.34144279,  0.94630077]]])

print(np.shape(x))

def image2vector(image):
	x = image
	v = image.reshape(image.shape[0] * image.shape[1] * image.shape[2], 1)
	w = x.reshape(image.shape[0] * image.shape[1], 2)
	return v, w

v, w = image2vector(x)

#print("image2vector(image) : " + str(image2vector(x)))
#print(np.shape(image2vector(x)))
print("(18, 1): " + str(v))
print("(9, 2): " + str(w))