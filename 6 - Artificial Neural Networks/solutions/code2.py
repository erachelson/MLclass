### WRITE YOUR CODE HERE
# If you get stuck, uncomment the line above to load a correction in this cell (then you can execute this code).

ypred,zpred = forward_pass(X, verbose=True)
pred = zpred[-1]
err = np.mean((pred-y)**2)
print("Loss function estimate:",err)

