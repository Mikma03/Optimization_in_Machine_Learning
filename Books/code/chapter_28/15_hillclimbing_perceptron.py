# hill climbing to optimize weights of a perceptron model for classification
from numpy import asarray
from numpy.random import randn
from numpy.random import rand
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# transfer function
def transfer(activation):
	if activation >= 0.0:
		return 1
	return 0

# activation function
def activate(row, weights):
	# add the bias, the last weight
	activation = weights[-1]
	# add the weighted input
	for i in range(len(row)):
		activation += weights[i] * row[i]
	return activation

# # use model weights to predict 0 or 1 for a given row of data
def predict_row(row, weights):
	# activate for input
	activation = activate(row, weights)
	# transfer for activation
	return transfer(activation)

# use model weights to generate predictions for a dataset of rows
def predict_dataset(X, weights):
	yhats = list()
	for row in X:
		yhat = predict_row(row, weights)
		yhats.append(yhat)
	return yhats

# objective function
def objective(X, y, weights):
	# generate predictions for dataset
	yhat = predict_dataset(X, weights)
	# calculate accuracy
	score = accuracy_score(y, yhat)
	return score

# hill climbing local search algorithm
def hillclimbing(X, y, objective, solution, n_iter, step_size):
	# evaluate the initial point
	solution_eval = objective(X, y, solution)
	# run the hill climb
	for i in range(n_iter):
		# take a step
		candidate = solution + randn(len(solution)) * step_size
		# evaluate candidate point
		candidte_eval = objective(X, y, candidate)
		# check if we should keep the new point
		if candidte_eval >= solution_eval:
			# store the new point
			solution, solution_eval = candidate, candidte_eval
			# report progress
			print('>%d %.5f' % (i, solution_eval))
	return [solution, solution_eval]

# define dataset
X, y = make_classification(n_samples=1000, n_features=5, n_informative=2, n_redundant=1, random_state=1)
# split into train test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)
# define the total iterations
n_iter = 1000
# define the maximum step size
step_size = 0.05
# determine the number of weights
n_weights = X.shape[1] + 1
# define the initial solution
solution = rand(n_weights)
# perform the hill climbing search
weights, score = hillclimbing(X_train, y_train, objective, solution, n_iter, step_size)
print('Done!')
print('f(%s) = %f' % (weights, score))
# generate predictions for the test dataset
yhat = predict_dataset(X_test, weights)
# calculate accuracy
score = accuracy_score(y_test, yhat)
print('Test Accuracy: %.5f' % (score * 100))
