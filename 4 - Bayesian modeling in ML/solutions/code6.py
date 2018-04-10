### WRITE YOUR CODE HERE
# If you get stuck, uncomment the line above to load a correction in this cell (then you can execute this code).

from sklearn.gaussian_process import GaussianProcessClassifier

spam_GP = GaussianProcessClassifier()
print(spam_GP.fit(Xtrain.toarray(),ytrain))

print("Score:",spam_GP.score(Xtest.toarray(),ytest))
