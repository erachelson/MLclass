### WRITE YOUR CODE HERE
# If you get stuck, uncomment the line above to load a correction in this cell (then you can execute this code).

spam_GP = GaussianProcessClassifier()
spam_GP.fit(Xtrain.toarray(),ytrain)
spam_GP.score(Xtest.toarray(),ytest)
