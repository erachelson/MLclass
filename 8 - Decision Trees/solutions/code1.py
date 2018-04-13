### WRITE YOUR CODE HERE
# If you get stuck, uncomment the line above to load a correction in this cell (then you can execute this code).

spam_dt = tree.DecisionTreeClassifier(criterion='entropy', max_depth=20, min_samples_leaf=10)
spam_dt.fit(Xtrain,ytrain)

print("score:", spam_dt.score(Xtest,ytest))
disp_tree('spam_dt',spam_dt)

# Compute cross-validation score
nb_trials = 30
score = []
for i in range(nb_trials):
    Xtrain, ytrain, Xtest, ytest = spam_data.shuffle_and_split(2000)
    spam_dt = tree.DecisionTreeClassifier(criterion='entropy', max_depth=20, min_samples_leaf=10)
    spam_dt.fit(Xtrain,ytrain)
    score += [spam_dt.score(Xtest,ytest)]
    print('*', end='')
print(" done!")

print("Average generalization score:", np.mean(score))
print("Standard deviation:", np.std(score))
