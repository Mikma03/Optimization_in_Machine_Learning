# linear regression model
from numpy.random import rand
from sklearn.datasets import make_regression
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

# define dataset
X, y = make_regression(n_samples=1000, n_features=10, n_informative=2, noise=0.2, random_state=1)
# determine the number of coefficients
n_coeff = X.shape[1] + 1
# generate random coefficients
coefficients = rand(n_coeff)
# generate predictions for dataset
yhat = predict_dataset(X, coefficients)
# calculate model prediction error
score = mean_squared_error(y, yhat)
print('MSE: %f' % score)
