### WRITE YOUR CODE HERE
# If you get stuck, uncomment the line above to load a correction in this cell (then you can execute this code).

opt_all = np.array([minimize(like_obj, th, method='SLSQP', bounds=[(1e-6,25)]) for th in theta_start])

