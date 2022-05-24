# logistic regression function for binary classification
from math import exp
from numpy.random import rand
from sklearn.datasets import make_classification
from sklearn.metrics import accuracy_score

# logistic regression
def predict_row(row, coefficients):
	# add the bias, the last coefficient
	result = coefficients[-1]
	# add the weighted input
	for i in range(len(row)):
		result += coefficients[i] * row[i]
	# logistic function
	logistic = 1.0 / (1.0 + exp(-result))
	return logistic

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
X, y = make_classification(n_samples=1000, n_features=5, n_informative=2, n_redundant=1, random_state=1)
# determine the number of coefficients
n_coeff = X.shape[1] + 1
# generate random coefficients
coefficients = rand(n_coeff)
# generate predictions for dataset
yhat = predict_dataset(X, coefficients)
# round predictions to labels
yhat = [round(y) for y in yhat]
# calculate accuracy
score = accuracy_score(y, yhat)
print('Accuracy: %f' % score)
