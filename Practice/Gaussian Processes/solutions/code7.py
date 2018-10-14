### WRITE YOUR CODE HERE
# If you get stuck, uncomment the line above to load a correction in this cell (then you can execute this code).

for k in range(n_iter):
    x_start = np.atleast_2d(np.random.rand(15)*25).T
    f_min_k = np.min(y_data)
    gpr.fit(x_data,y_data)
    obj_k = lambda x: -EI(gpr,np.atleast_2d(x),f_min_k)
    ## UNCOMMENT ONE OF THE INFILL CRITERIA
    # obj_k = lambda x: -EI(gpr,np.atleast_2d(x),f_min_k)
    # obj_k = lambda x: SBO(gpr,np.atleast_2d(x))
    # obj_k = lambda x: UCB(gpr,np.atleast_2d(x))
    
    opt_all = np.array([minimize(obj_k, x_st, method='SLSQP', bounds=[(0,25)]) for x_st in x_start])
    opt_success = opt_all[[opt_i['success'] for opt_i in opt_all]]
    obj_success = np.array([opt_i['fun'] for opt_i in opt_success])
    ind_min = np.argmin(obj_success)
    opt = opt_success[ind_min]
    x_et_k = opt['x']
    
    y_et_k = fun(x_et_k)
    
    y_data = np.atleast_2d(np.append(y_data,y_et_k)).T
    x_data = np.atleast_2d(np.append(x_data,x_et_k)).T
    
ind_best = np.argmin(y_data)
x_opt = x_data[ind_best]
y_opt = y_data[ind_best]

