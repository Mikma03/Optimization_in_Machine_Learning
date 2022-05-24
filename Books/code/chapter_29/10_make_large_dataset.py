# define a large classification dataset
from sklearn.datasets import make_classification
# define dataset
X, y = make_classification(n_samples=10000, n_features=500, n_informative=10, n_redundant=490, random_state=1)
# summarize the shape of the dataset
print(X.shape, y.shape)
