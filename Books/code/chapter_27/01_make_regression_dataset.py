# define a regression dataset
from sklearn.datasets import make_regression
# define dataset
X, y = make_regression(n_samples=1000, n_features=10, n_informative=2, noise=0.2, random_state=1)
# summarize the shape of the dataset
print(X.shape, y.shape)
