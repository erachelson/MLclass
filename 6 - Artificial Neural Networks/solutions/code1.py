### WRITE YOUR CODE HERE
# If you get stuck, uncomment the line above to load a correction in this cell (then you can execute this code).

input_value = np.array([[1,2]])

def forward_pass(x, verbose=False):
    z = [np.zeros((x.shape[0], sz)) for sz in sizes]
    y = [np.zeros((x.shape[0], sz)) for sz in sizes]
    z[0] = x.copy()
    for i in range(1,len(sizes)):
        if verbose:
            print("# Forward propagation to layer", i)
        y[i] = np.dot(z[i-1],weights[i-1].T) + biases[i-1]
        if verbose:
            print("Neuron inputs:", y[i])
        if i==len(sizes)-1:
            z[i] = y[i]
        else:
            z[i] = sigmoid(y[i])
        if verbose:
            print("Layer outputs:", z[i])
    return y,z

y,z = forward_pass(input_value, verbose=True)
