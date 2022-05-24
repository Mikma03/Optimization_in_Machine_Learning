# example of a 2d objective function

# objective function
def objective(x, y):
	return x**2.0 + y**2.0

# evaluate inputs to the objective function
x = 4.0
y = 4.0
result = objective(x, y)
print('f(%.3f, %.3f) = %.3f' % (x, y, result))
