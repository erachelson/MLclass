import numpy as np
import matplotlib.pyplot as plt

def plot_SVC(model, X, y):
    fig_size = (6, 6)
    fig=plt.figure(figsize=fig_size, dpi= 80, facecolor='w', edgecolor='k')
    Xblue = X[y==-1]
    Xred  = X[y==+1]
    plt.scatter(Xblue[:,0],Xblue[:,1],c='c')
    plt.scatter(Xred[:,0],Xred[:,1],c='r')
    XX, YY = np.meshgrid(np.arange(np.min(X[:,0]),np.max(X[:,0]),0.1), np.arange(np.min(X[:,1]),np.max(X[:,1]),0.1))
    ZZ = model.decision_function(np.c_[XX.ravel(), YY.ravel()])
    ZZ = ZZ.reshape(XX.shape)
    plt.contour(XX, YY, ZZ, levels=[0],alpha=0.75)
    fig=plt.figure(figsize=fig_size, dpi= 80, facecolor='w', edgecolor='k')
    cont = plt.contour(XX, YY, ZZ, levels=[-1., 0., 1.], alpha=0.75)
    #plt.clabel(cont, cont.levels, inline=True, fontsize=10, cmap = plt.cm.coolwarm)
    #fig=plt.figure(figsize=fig_size, dpi= 80, facecolor='w', edgecolor='k')
    #cont = plt.contourf(XX, YY, ZZ, alpha=0.75, cmap = plt.cm.coolwarm)
