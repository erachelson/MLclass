### WRITE YOUR CODE HERE
# If you get stuck, uncomment the line above to load a correction in this cell (then you can execute this code).

Nsteps = 100
forest = list()
sample_weights = np.ones(len(y))/len(y)
tree_weights = np.zeros(Nsteps)
single_tree_training_error = np.zeros(Nsteps)
overall_training_error = np.zeros(Nsteps)
generalization_error = np.zeros(Nsteps)
for i in range(Nsteps):
    # Train tree
    dt = tree.DecisionTreeClassifier(criterion='entropy',max_depth=3)
    dt.fit(X,y,sample_weight=sample_weights)
    # Compute error
    y_pred = dt.predict(X)
    classif_error = sum(np.not_equal(y_pred, y)*sample_weights) / sum(sample_weights)
    forest.append(dt)
    # Get tree weight
    alpha = .5*np.log((1-classif_error)/classif_error)
    tree_weights[i] = alpha
    # Update weights
    sample_weights = sample_weights*np.exp(-alpha*y_pred*y)
    sample_weights = sample_weights/sum(sample_weights)
    # Plot and store data
    #plot_decision_boundary_forest(forest, sample_weights, X, y)
    single_tree_training_error[i] = classif_error
    y_pred = forest_predict(forest, tree_weights, X)
    overall = sum(np.not_equal(y_pred, y))/len(y)
    overall_training_error[i] = overall
    y_pred = forest_predict(forest, tree_weights, Xtest)
    gen = sum(np.not_equal(y_pred, ytest))/len(ytest)
    generalization_error[i] = gen
    #print("Nb trees %d. Last tree error %.3g. Training error %.3g. Generalization error %.3g. Press Enter"
    #      %(len(forest),classif_error, overall, gen))
    #input()

plt.figure(figsize=(8,8))
plt.plot(single_tree_training_error,c='b')
plt.plot(overall_training_error,c='r')
plt.plot(generalization_error,c='g')
plt.show()
plot_decision_boundary_forest(forest, sample_weights, X, y)
