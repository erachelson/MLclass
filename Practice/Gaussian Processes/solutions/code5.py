### WRITE YOUR CODE HERE
# If you get stuck, uncomment the line above to load a correction in this cell (then you can execute this code).

ker = SEkernel()
gpr = GP(kernel=ker,n_restarts_optimizer=10,normalize_y=True)

gpr.fit(x_data,y_data)

