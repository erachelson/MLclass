import numpy as np

class ann:
    """Multi-layered neural network (fully connected) for regression with sigmoid activation functions"""
    def __init__(self, sizes):
        self.layer_sizes = sizes
        self.biases = [np.random.randn(1,y) for y in self.layer_sizes[1:]]
        self.weights = [np.random.randn(out,inp) for inp,out in zip(self.layer_sizes[:-1],self.layer_sizes[1:])]
        return
    def __call__(self, x):
        return self.forward_pass(x)
    def reset_weights(self):
        self.biases = [np.random.randn(1,y) for y in self.layer_sizes[1:]]
        self.weights = [np.random.randn(out,inp) for inp,out in zip(self.layer_sizes[:-1],self.layer_sizes[1:])]
    def sigmoid(self,z):
        """The sigmoid function.

        Parameters
        ----------
        z : np.array
            Input array of N scalar values. Should be a Nx1 array

        Returns
        -------
        np.array : 
            The value of the sigmoid function in each of the N input scalars. Array of size Nx1.
        np.array :
            The derivative of the sigmoid function in each of the N input scalars. Array of size Nx1.
        """
        val = 1.0/(1.0+np.exp(-z))
        der = val*(1.-val)
        return val, der
    def forward_pass(self, x, verbose=False):
        """Forward propagation of x through the network.

        Parameters
        ----------
        x : np.array
            The input minibatch with N elements of dimension p. Should be a Nxp array.
        verbose : boolean, optional
            Indicates whether to print intermediate layer inputs and activations.

        Returns
        -------
        list :
            A list of layer-wise input arrays of shape N x layer_size
        list :
            A list of layer-wise activation derivative arrays of shape N x layer_size
        list :
            A list of layer-wise activation arrays of shape N x layer_size
        """
        z = [np.zeros((x.shape[0], sz)) for sz in self.layer_sizes]
        s = [np.zeros((x.shape[0], sz)) for sz in self.layer_sizes]
        y = [np.zeros((x.shape[0], sz)) for sz in self.layer_sizes]
        z[0] = x.copy()
        for i in range(1,len(self.layer_sizes)):
            if verbose:
                print("# Forward propagation to layer", i)
            y[i] = np.dot(z[i-1],self.weights[i-1].T) + self.biases[i-1]
            if verbose:
                print("Neuron inputs:", y[i])
            if i==len(self.layer_sizes)-1:
                s[i] = np.ones((x.shape[0],self.layer_sizes[-1]))
                z[i] = y[i]
            else:
                v,d  = self.sigmoid(y[i])
                s[i] = d
                z[i] = v
            if verbose:
                print("Layer outputs:", z[i])
        return y,s,z
    def backward_pass(self, out, y, s, z, alpha):
        """Gradient step on the network weights
        
        Parameters
        ----------
        out : np.array
            The target minibatch with N elements. Should be a Nx1 array.
        y : np.array
            The inputs to each layer computed during the forward pass on the input minibatch with N elements. Should be a list of N x layer_size arrays.
        z : np.array
            The activations of each layer computed during the forward pass on the input minibatch with N elements. Should be a list of N x layer_size arrays.
        s : np.array
            The derivatives of each layer's activation computed during the forward pass on the input minibatch with N elements. Should be a list of N x layer_size arrays.
        alpha : float
            The learning rate.
        """
        delta = [np.zeros((out.shape[0], sz)) for sz in self.layer_sizes]
        error = z[-1] - out
        for i in range(len(self.layer_sizes)-1,0,-1):
            # compute delta
            if i==len(self.layer_sizes)-1:
                delta[i] = s[-1]
            else:
                delta[i] = np.dot(delta[i+1],self.weights[i])
                delta[i] = np.multiply(delta[i],s[i])
            # intermediate delta value that includes the error term 
            # (useful for minibatches since each element has a different error value)
            delta_temp = np.multiply(delta[i],error)
            # update weights
            grad_w = np.dot(delta_temp.T,z[i-1])
            grad_b = np.sum(delta_temp, axis=0)
            self.weights[i-1] -= alpha * grad_w
            self.biases[i-1]  -= alpha * grad_b
        return
    def train_on_minibatch(self, training_x, training_y, alpha):
        """Performs a forward and a backward pass on the input minibatch

        Parameters
        ----------
        training_x : np.array
            The input minibatch with N elements of dimension p. Should be a Nxp array.
        training_y : np.array
            The target minibatch with N elements. Should be a Nx1 array.
        alpha : float
            The learning rate.
        """
        y,s,z = self.forward_pass(training_x)
        self.backward_pass(training_y, y, s, z, alpha)
        return




