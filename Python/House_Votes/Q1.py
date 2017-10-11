from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import cross_validate
from copy import copy


y, y_discard = [], []
X_discard, X_value, X_impute = [], [], []
X_sum, X_sum_total = [0]*16, [0]*16
#Massage Data
def massage(x):
	if( x == 'y'):
		return 1
	elif(x == 'n'):
		return 0
	elif(x == '?'):
		return '?'

	print "There was a problem"
	return x

#Read in Data
with open('house-votes-84.data') as f:
	lines = f.readlines()
	
	for line in lines:

		line = line.strip().split(',')
		if(line[0] == 'republican'):
			y.append(1)
		else:
			y.append(0)

		X_train = [massage(elem) for elem in line[1:]]
	
		X_value.append(copy(X_train))
		X_impute.append(copy(X_train))

		#i) Discard instances that have missing feature values 
		if('?' not in line[1:]):
			X_discard.append(X_train)
			if(line[0] == 'republican'):
				y_discard.append(1)
			else:
				y_discard.append(0)

		for ii in range(len(X_train)):	
			if(X_train[ii] != '?'):
				X_sum[ii] += X_train[ii]
				X_sum_total[ii] += 1

#ii) treat "missing" as if it is a value
for elem in X_value:
	while('?' in elem):
		ind = elem.index('?')
		elem[ind] = 2


#Find most common value for each feature
X_sum = [1 if float(X_sum[ii])/X_sum_total[ii] >= .5 else 0 for ii in range(len(X_sum))]

#iii) Impute missing values
for elem in X_impute:
	while('?' in elem):
		ind = elem.index('?')
		elem[ind] = copy(X_sum[ind])

scoring = ['precision', 'recall', 'f1']
decision_tree = DecisionTreeClassifier(random_state = 5)
naive_bayes = GaussianNB()

#Perform 5-fold cross validation + print average precision, recall, and f1 for DecisionTree and Naive Bayes
for title, X_val, y_val in [("Discard Missing", X_discard, y_discard), ("Treat Missing as Value", X_value, y), ("Impute Missing", X_impute, y)]:
	print("\n" + title)
	
	score1 = cross_validate(decision_tree, X_val, y_val, scoring=scoring, cv=5, return_train_score=False)
	print "Decision_Tree: "
	for elem in score1:
		print elem, score1[elem] 
		print "Average:", float(sum(score1[elem]))/len(score1[elem])

	score2 = cross_validate(naive_bayes, X_val, y_val, scoring=scoring, cv=5, return_train_score=False)
	print "Naive Bayes:"

	for elem in score2:
		print elem, score2[elem]
		print "Average:", float(sum(score2[elem]))/len(score2[elem])

