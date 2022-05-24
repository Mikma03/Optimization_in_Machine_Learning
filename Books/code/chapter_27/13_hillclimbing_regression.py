# optimize linear regression coefficients for regression dataset
from numpy.random import randn
from numpy.random import rand
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# linear regression
def predict_row(row, coefficients):
	# add the bias, the last coefficient
	result = coefficients[-1]
	# add the weighted input
	for i in range(len(row)):
		result += coefficients[i] * row[i]
	return result

# use model coefficients to generate predictions for a dataset of rows
def predict_dataset(X, coefficients):
	yhats = list()
	for row in X:
		# make a prediction
		yhat = predict_row(row, coefficients)
		# store the prediction
		yhats.append(yhat)
	return yhats

# objective function
def objective(X, y, coefficients):
	# generate predictions for dataset
	yhat = predict_dataset(X, coefficients)
	# calculate accuracy
	score = mean_squared_error(y, yhat)
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
		if candidte_eval <= solution_eval:
			# store the new point
			solution, solution_eval = candidate, candidte_eval
			# report progress
			print('>%d %.5f' % (i, solution_eval))
	return [solution, solution_eval]

# define dataset
X, y = make_regression(n_samples=1000, n_features=10, n_informative=2, noise=0.2, random_state=1)
# split into train test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)
# define the total iterations
n_iter = 2000
# define the maximum step size
step_size = 0.15
# determine the number of coefficients
n_coef = X.shape[1] + 1
# define the initial solution
solution = rand(n_coef)
# perform the hill climbing search
coefficients, score = hillclimbing(X_train, y_train, objective, solution, n_iter, step_size)
print('Done!')
print('Coefficients: %s' % coefficients)
print('Train MSE: %f' % (score))
# generate predictions for the test dataset
yhat = predict_dataset(X_test, coefficients)
# calculate accuracy
score = mean_squared_error(y_test, yhat)
print('Test MSE: %f' % (score))
