# simple perceptron model for binary classification
from numpy.random import rand
from sklearn.datasets import make_classification
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

# use model weights to predict 0 or 1 for a given row of data
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

# define dataset
X, y = make_classification(n_samples=1000, n_features=5, n_informative=2, n_redundant=1, random_state=1)
# determine the number of weights
n_weights = X.shape[1] + 1
# generate random weights
weights = rand(n_weights)
# generate predictions for dataset
yhat = predict_dataset(X, weights)
# calculate accuracy
score = accuracy_score(y, yhat)
print(score)
