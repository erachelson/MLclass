### WRITE YOUR CODE HERE
# If you get stuck, uncomment the line above to load a correction in this cell (then you can execute this code).

import scipy.optimize as sopt

def func(x):
    """x = (M,w_1,w_2,b)"""
    return -x[0]

def ineq_constr(x):
    """x = (M,w_1,w_2,b)"""
    return y*(x[1]*X[:,0] + x[2]*X[:,1] + x[3]*np.ones(X.shape[0])) - x[0]*np.ones(X.shape[0])

def eq_const(x):
    return x[1]*x[1]+x[2]*x[2]-1

x0 = np.array([0.,0.7,-1.,0.4])
res = sopt.fmin_slsqp(func, x0, f_eqcons=eq_const, f_ieqcons=ineq_constr)
print(res)
print("margin =", res[0])
fig=plt.figure(figsize=fig_size, dpi= 80, facecolor='w', edgecolor='k')
plt.scatter(Xblue[:,0],Xblue[:,1],c='b')
plt.scatter(Xred[:,0],Xred[:,1],c='r')
XX = np.arange(-1.,12.,0.1)
YY = -(res[1]*XX+res[3])/res[2]
plt.plot(XX,YY,c='g')
YY = -(res[1]*XX+res[3]+res[0])/res[2]
plt.plot(XX,YY,'g--')
YY = -(res[1]*XX+res[3]-res[0])/res[2]
plt.plot(XX,YY,'g--');

