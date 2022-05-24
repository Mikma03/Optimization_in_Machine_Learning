# stochastic optimization for feature selection
from numpy import mean
from numpy.random import rand
from numpy.random import choice
from sklearn.datasets import make_classification
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier

# objective function
def objective(X, y, subset):
	# convert into column indexes
	ix = [i for i, x in enumerate(subset) if x]
	# check for now column (all False)
	if len(ix) == 0:
		return 0.0
	# select columns
	X_new = X[:, ix]
	# define model
	model = DecisionTreeClassifier()
	# evaluate model
	scores = cross_val_score(model, X_new, y, scoring='accuracy', cv=3, n_jobs=-1)
	# summarize scores
	result = mean(scores)
	return result, ix

# mutation operator
def mutate(solution, p_mutate):
	# make a copy
	child = solution.copy()
	for i in range(len(child)):
		# check for a mutation
		if rand() < p_mutate:
			# flip the inclusion
			child[i] = not child[i]
	return child

# hill climbing local search algorithm
def hillclimbing(X, y, objective, n_iter, p_mutate):
	# generate an initial point
	solution = choice([True, False], size=X.shape[1])
	# evaluate the initial point
	solution_eval, ix = objective(X, y, solution)
	# run the hill climb
	for i in range(n_iter):
		# take a step
		candidate = mutate(solution, p_mutate)
		# evaluate candidate point
		candidate_eval, ix = objective(X, y, candidate)
		# check if we should keep the new point
		if candidate_eval >= solution_eval:
			# store the new point
			solution, solution_eval = candidate, candidate_eval
		# report progress
		print('>%d f(%s) = %f' % (i+1, len(ix), solution_eval))
	return solution, solution_eval

# define dataset
X, y = make_classification(n_samples=10000, n_features=500, n_informative=10, n_redundant=490, random_state=1)
# define the total iterations
n_iter = 100
# probability of including/excluding a column
p_mut = 10.0 / 500.0
# perform the hill climbing search
subset, score = hillclimbing(X, y, objective, n_iter, p_mut)
# convert into column indexes
ix = [i for i, x in enumerate(subset) if x]
print('Done!')
print('Best: f(%d) = %f' % (len(ix), score))
