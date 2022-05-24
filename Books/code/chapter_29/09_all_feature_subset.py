# feature selection by enumerating all possible subsets of features
from itertools import product
from numpy import mean
from sklearn.datasets import make_classification
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.tree import DecisionTreeClassifier
# define dataset
X, y = make_classification(n_samples=1000, n_features=5, n_informative=2, n_redundant=3, random_state=1)
# determine the number of columns
n_cols = X.shape[1]
best_subset, best_score = None, 0.0
# enumerate all combinations of input features
for subset in product([True, False], repeat=n_cols):
	# convert into column indexes
	ix = [i for i, x in enumerate(subset) if x]
	# check for now column (all False)
	if len(ix) == 0:
		continue
	# select columns
	X_new = X[:, ix]
	# define model
	model = DecisionTreeClassifier()
	# define evaluation procedure
	cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=3, random_state=1)
	# evaluate model
	scores = cross_val_score(model, X_new, y, scoring='accuracy', cv=cv, n_jobs=-1)
	# summarize scores
	result = mean(scores)
	# report progress
	print('>f(%s) = %f ' % (ix, result))
	# check if it is better than the best so far
	if best_score is None or result >= best_score:
		# better result
		best_subset, best_score = ix, result
# report best
print('Done!')
print('f(%s) = %f' % (best_subset, best_score))
