### WRITE YOUR CODE HERE
# If you get stuck, uncomment the line above to load a correction in this cell (then you can execute this code).

def compute_K(X,sigma_kernel,l,sigma_noise):
    ### FILL THE VALUES OF K
    N = X.shape[0]
    K = np.zeros((N,N))
    for i in range(N):
        for j in range(N):
            K[i,j] = kernel(X[i],X[j],sigma_kernel,l,sigma_noise)
    return K

def GPpredict(x_new, x_data, y_data, Kinv):
    ### COMPUTE MEAN AND STANDARD DEVIATION
    N = y_data.shape[0]
    Kstar = np.zeros((1,N))
    for i in range(N):
        Kstar[0,i] = kernel(x_data[i], x_new, sigma_kernel, l, sigma_noise)
    mu = Kstar @ Kinv @ y_data
    sigma = kernel(x_new,x_new,sigma_kernel,l,sigma_noise) - Kstar @ Kinv @ Kstar.T
    return mu, sigma

