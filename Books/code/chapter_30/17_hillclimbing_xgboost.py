# xgboost manual hyperparameter optimization for binary classification
from numpy import mean
from numpy.random import randn
from numpy.random import rand
from numpy.random import randint
from sklearn.datasets import make_classification
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RepeatedStratifiedKFold
from xgboost import XGBClassifier

# objective function
def objective(X, y, cfg):
	# unpack config
	lrate, n_tree, subsam, depth = cfg
	# define model
	model = XGBClassifier(learning_rate=lrate, n_estimators=n_tree, subsample=subsam, max_depth=depth, use_label_encoder=False, eval_metric="logloss")
	# define evaluation procedure
	cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=3, random_state=1)
	# evaluate model
	scores = cross_val_score(model, X, y, scoring='accuracy', cv=cv, n_jobs=-1)
	# calculate mean accuracy
	result = mean(scores)
	return result

# take a step in the search space
def step(cfg):
	# unpack config
	lrate, n_tree, subsam, depth = cfg
	# learning rate
	lrate = lrate + randn() * 0.01
	if lrate <= 0.0:
		lrate = 1e-8
	if lrate > 1:
		lrate = 1.0
	# number of trees
	n_tree = round(n_tree + randn() * 50)
	if n_tree <= 0.0:
		n_tree = 1
	# subsample percentage
	subsam = subsam + randn() * 0.1
	if subsam <= 0.0:
		subsam = 1e-8
	if subsam > 1:
		subsam = 1.0
	# max tree depth
	depth = round(depth + randn() * 7)
	if depth <= 1:
		depth = 1
	# return new config
	return [lrate, n_tree, subsam, depth]

# hill climbing local search algorithm
def hillclimbing(X, y, objective, n_iter):
	# starting point for the search
	solution = step([0.1, 100, 1.0, 7])
	# evaluate the initial point
	solution_eval = objective(X, y, solution)
	# run the hill climb
	for i in range(n_iter):
		# take a step
		candidate = step(solution)
		# evaluate candidate point
		candidate_eval = objective(X, y, candidate)
		# check if we should keep the new point
		if candidate_eval >= solution_eval:
			# store the new point
			solution, solution_eval = candidate, candidate_eval
			# report progress
			print('>%d, cfg=[%s] %.5f' % (i, solution, solution_eval))
	return [solution, solution_eval]

# define dataset
X, y = make_classification(n_samples=1000, n_features=5, n_informative=2, n_redundant=1, random_state=1)
# define the total iterations
n_iter = 200
# perform the hill climbing search
cfg, score = hillclimbing(X, y, objective, n_iter)
print('Done!')
print('cfg=[%s]: Mean Accuracy: %f' % (cfg, score))
