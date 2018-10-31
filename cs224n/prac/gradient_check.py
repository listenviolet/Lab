import numpy as np 

def eval_numerical_gradient(f,x):
	"""
	a naive implementation of numerical gradient of f at x
	- f shoule be a function that takes a single argument
	- x is the point (numpy array) to evaluate the gradient at
	"""

	grad = np.zeros(x.shape)
	h = 0.0001

	# iterate over all indexes in x
	it = np.nditer(x, flag = ['multi_index'], op_flags = ['readwrite'])

	while not it.finished:
		ix = it.multi_index
		old_value = x[ix]

		x[ix] = old_value + h
		fxh_left = f(x)

		x[ix] = old_value - h
		fxh_right = f(x)

		x[ix] = old_value

		# compute the partial derivative
		grad[ix] = (fxh_left - fxh_right) / (2 * h)
		it.iterate()

	return grad