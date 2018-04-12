### WRITE YOUR CODE HERE
# If you get stuck, uncomment the line above to load a correction in this cell (then you can execute this code).

sigma_kernel = 0.2
l=0.3
def kernel(x1,x2,sigma_kernel,l,sigma_noise):
    return sigma_kernel * sigma_kernel * np.exp(-(x1-x2)**2 / (2*l*l)) + sigma_noise*(x1==x2)

def compute_K(X,sigma_kernel,l,sigma_noise):
    ### FILL THE VALUES OF K
    N = X.shape[0]
    K = np.zeros((N,N))
    for i in range(N):
        for j in range(N):
            K[i,j] = kernel(X[i],X[j],sigma_kernel,l,sigma_noise)
    return K

Kinv = np.linalg.inv(compute_K(X,sigma_kernel,l,sigma_noise))

def GPpredict(x_new, x_data, y_data, Kinv):
    ### COMPUTE MEAN AND STANDARD DEVIATION
    N = y_data.shape[0]
    Kstar = np.zeros((1,N))
    for i in range(N):
        Kstar[0,i] = kernel(x_data[i], x_new, sigma_kernel, l, sigma_noise)
    mu = Kstar @ Kinv @ y_data
    sigma = kernel(x_new,x_new,sigma_kernel,l,sigma_noise) - Kstar @ Kinv @ Kstar.T
    return mu, sigma

x = np.linspace(-5,10,100)
y = np.zeros(x.shape)
sigma = np.zeros(x.shape)
for i in range(x.shape[0]):
    y[i], sigma[i] = GPpredict(x[i], X, Y, Kinv)

fig=plt.figure(figsize=(5,5), dpi= 80, facecolor='w', edgecolor='k')
plt.plot(x, func(x), 'r:', label=u'$f(x) = x\,\sin(x)$')
plt.plot(X, Y, 'r.', markersize=10, label=u'Observations')
plt.plot(x, y, 'b-', label=u'Prediction')
plt.fill(np.concatenate([x, x[::-1]]),
         np.concatenate([y - 1.9600 * sigma,
                        (y + 1.9600 * sigma)[::-1]]),
         alpha=.5, fc='b', ec='None', label='95% confidence interval')
plt.xlabel('$x$')
plt.ylabel('$f(x)$')
plt.ylim(-6, 10)
plt.legend(loc='upper left');
