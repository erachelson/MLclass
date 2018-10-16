### WRITE YOUR CODE HERE - implement your own version of k-fold cross-validation.
# If you get stuck, uncomment the line above to load a correction in this cell (then you can execute this code).

def split_data(X, y, start, end):
    X_train = np.concatenate((X[:start], X[end:]), axis=0)
    y_train = np.concatenate((y[:start], y[end:]), axis=0)
    X_test  = X[start:end]
    y_test  = y[start:end]
    return X_train, y_train, X_test, y_test

accuracy = []

for c in C:
    accuracies = []
    for i in range(k):
        X_train, y_train, X_test, y_test = split_data(X, y, i*n, (i+1)*n)
        mySVC = svm.SVC(kernel='linear', C=c)
        mySVC.fit(X_train, y_train)
        y_pred = mySVC.predict(X_test)
        acc = mySVC.score(X_test, y_test)
        accuracies.append(acc)
    accuracy.append(np.mean(accuracies))
    
for acc, c in zip(accuracy, C):
    print(c, "\t --> \t", acc)

plt.plot(np.log(C),np.log(accuracy));

