# calculate the derivative of the objective function

# derivative of objective function
def derivative(x):
	return x * 2.0

# calculate derivatives
d1 = derivative(-0.5)
print("f'(-0.5) = %.3f" % d1)
d2 = derivative(0.5)
print("f'(0.5) = %.3f" % d2)
d3 = derivative(0.0)
print("f'(0.0) = %.3f" % d3)
