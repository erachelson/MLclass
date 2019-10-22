### WRITE YOUR CODE HERE
# If you get stuck, uncomment the line above to load a correction in this cell (then you can execute this code).



gpr = KRG(theta0=[1e-2]*x_data.shape[0],print_prediction = False)
gpr.set_training_values(x_data,y_data)

gpr.train()
