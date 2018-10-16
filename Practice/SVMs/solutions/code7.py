### WRITE YOUR CODE HERE
# If you get stuck, uncomment the line above to load a correction in this cell (then you can execute this code).

from sklearn.grid_search import RandomizedSearchCV
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=4)

mySVC = svm.SVC(kernel='linear')
mySVC.fit(X_train, y_train)
y_pred = mySVC.predict(X_test)
y_test = y_test[:].tolist()

error = 0
for i in range(len(y_pred)):
    if not (y_pred[i] == y_test[i]):
        error += 1
error_rate = error / len(y_pred)
print('Number of errors : ', error)
print('Error rate       : ', error_rate)
