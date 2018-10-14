### WRITE YOUR CODE HERE
# If you get stuck, uncomment the line above to load a correction in this cell (then you can execute this code).

def likelihood(x_data,y_data,theta,sig):
    K = cov_matrix(x_data,theta,sig)
    args1 = y_data.T.dot(np.linalg.inv(K))
    args2 = np.log(args1.dot(y_data)/x_data.shape[0])
    args3 =  np.log(np.linalg.det(K))
    like = 0.5*(x_data.shape[0])*args2 + args3
    return like[0,0]


