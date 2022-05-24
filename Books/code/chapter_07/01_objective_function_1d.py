# example of a 1d objective function

# objective function
def objective(x):
	return x**2.0

# evaluate inputs to the objective function
x = 4.0
result = objective(x)
print('f(%.3f) = %.3f' % (x, result))
