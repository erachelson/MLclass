### WRITE YOUR CODE HERE
# If you get stuck, uncomment the line above to load a correction in this cell (then you can execute this code).

w = np.array([0.7, -1])
w = w/np.linalg.norm(w)
w0 = 0.4/np.linalg.norm(w)
M = y*(np.dot(X,w) + w0)
print("margin =", np.min(M))
