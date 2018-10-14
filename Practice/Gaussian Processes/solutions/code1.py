### WRITE YOUR CODE HERE
# If you get stuck, uncomment the line above to load a correction in this cell (then you can execute this code).

def myGPpredict(x_new, x_data, y_data, K_inv, theta, sig):
    K_et = cov_vect(x_new,x_data,theta,sig)
    mu = K_et.dot(K_inv.dot(y_data))
    k_xx = cov_function(x_new,x_new,theta,sig)
    sigma = k_xx - K_et.dot(K_inv.dot(K_et.T))
    return mu[0],sigma
