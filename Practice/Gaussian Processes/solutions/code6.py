### WRITE YOUR CODE HERE
# If you get stuck, uncomment the line above to load a correction in this cell (then you can execute this code).

def EI(GP,points,f_min):
    pred = GP.predict(points,return_std=True)
    args0 = (f_min - pred[0])/np.atleast_2d(pred[1]).T
    args1 = (f_min - pred[0])*norm.cdf(args0)
    args2 = np.atleast_2d(pred[1]).T*norm.pdf(args0)
    ei = args1 + args2
    return ei


