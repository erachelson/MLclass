### WRITE YOUR CODE HERE
# If you get stuck, uncomment the line above to load a correction in this cell (then you can execute this code).

K = cov_matrix(x_data,theta,sig)
K_inv = np.linalg.inv(K)

y_pred = np.array([myGPpredict(x_t,x_data,y_data,K_inv,theta,sig) \
                   for x_t in x_test])

