### WRITE YOUR CODE HERE
# If you get stuck, uncomment the line above to load a correction in this cell (then you can execute this code).

## Data set "data/data2.csv"
X, y = load_data("data/data2.csv")
my_kernel = 'rbf'
mySVC = svm.SVC(kernel=my_kernel)
mySVC.fit(X,y)
plot_SVC(mySVC, X, y)

## Data set "data/data3.csv"
def my_kernel(X1, X2):
    n = len(X1)
    K = np.zeros(shape=(n,n))
    for i in range(n):
        for j in range(n):
            print('Can you find the optimal value of Surprise_value?')
            K[i][j] = np.cos(Surprise_value * X1[i][0]) * np.cos(Surprise_value * X2[j][0])
    return K
X, y = load_data("data/data3.csv")
mySVC = svm.SVC(kernel=my_kernel)
mySVC.fit(X,y)
plot_SVC(mySVC, X, y)

## Data set "data/data4.csv"
X, y = load_data("data/data4.csv")
my_kernel = 'linear'
mySVC = svm.SVC(kernel=my_kernel)
mySVC.fit(X,y)
plot_SVC(mySVC, X, y)
