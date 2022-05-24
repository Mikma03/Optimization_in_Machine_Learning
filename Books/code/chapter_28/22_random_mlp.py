# develop an mlp model for classification
from math import exp
from numpy.random import rand
from sklearn.datasets import make_classification
from sklearn.metrics import accuracy_score

# transfer function
def transfer(activation):
	# sigmoid transfer function
	return 1.0 / (1.0 + exp(-activation))

# activation function
def activate(row, weights):
	# add the bias, the last weight
	activation = weights[-1]
	# add the weighted input
	for i in range(len(row)):
		activation += weights[i] * row[i]
	return activation

# activation function for a network
def predict_row(row, network):
	inputs = row
	# enumerate the layers in the network from input to output
	for layer in network:
		new_inputs = list()
		# enumerate nodes in the layer
		for node in layer:
			# activate the node
			activation = activate(inputs, node)
			# transfer activation
			output = transfer(activation)
			# store output
			new_inputs.append(output)
		# output from this layer is input to the next layer
		inputs = new_inputs
	return inputs[0]

# use model weights to generate predictions for a dataset of rows
def predict_dataset(X, network):
	yhats = list()
	for row in X:
		yhat = predict_row(row, network)
		yhats.append(yhat)
	return yhats

# define dataset
X, y = make_classification(n_samples=1000, n_features=5, n_informative=2, n_redundant=1, random_state=1)
# determine the number of inputs
n_inputs = X.shape[1]
# one hidden layer and an output layer
n_hidden = 10
hidden1 = [rand(n_inputs + 1) for _ in range(n_hidden)]
output1 = [rand(n_hidden + 1)]
network = [hidden1, output1]
# generate predictions for dataset
yhat = predict_dataset(X, network)
# round the predictions
yhat = [round(y) for y in yhat]
# calculate accuracy
score = accuracy_score(y, yhat)
print(score)
