# plot a convex target function
from numpy import arange
from matplotlib import pyplot

# objective function
def objective(x):
	return (5.0 + x)**2.0

# define range
r_min, r_max = -10.0, 10.0
# prepare inputs
inputs = arange(r_min, r_max, 0.1)
# compute targets
targets = [objective(x) for x in inputs]
# plot inputs vs target
pyplot.plot(inputs, targets, '--')
pyplot.show()
