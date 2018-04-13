### WRITE YOUR CODE HERE
# If you get stuck, uncomment the line above to load a correction in this cell (then you can execute this code).

for i in range(Nbootstrap):
    Xb, yb = resample(X, y)
    dt = tree.DecisionTreeClassifier(criterion='entropy')
    dt.fit(Xb,yb)
    forest.append(dt)
    # Eval
    tree_training_error[i]=1.-dt.score(X,y)
    tree_generalization_error[i] = 1.-dt.score(Xtest,ytest)
    forest_training_error[i]=forest_score(forest,X,y)
    forest_generalization_error[i]=forest_score(forest,Xtest,ytest)
