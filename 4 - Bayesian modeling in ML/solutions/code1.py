### WRITE YOUR CODE HERE
# If you get stuck, uncomment the line above to load a correction in this cell (then you can execute this code).

# Estimate distribution parameters for males
dataM = data[data[:,0]==0]
mu_HS0 = np.mean(dataM[:,1])
std_HS0 = np.std(dataM[:,1])
mu_WS0 = np.mean(dataM[:,2])
std_WS0 = np.std(dataM[:,2])
mu_FS0 = np.mean(dataM[:,3])
std_FS0 = np.std(dataM[:,3])
pS0 = dataM.shape[0]/data.shape[0]

# Estimate distribution parameters for females
dataF = data[data[:,0]==1]
mu_HS1 = np.mean(dataF[:,1])
std_HS1 = np.std(dataF[:,1])
mu_WS1 = np.mean(dataF[:,2])
std_WS1 = np.std(dataF[:,2])
mu_FS1 = np.mean(dataF[:,3])
std_FS1 = np.std(dataF[:,3])
pS1 = dataF.shape[0]/data.shape[0]

# score that (H=1.81,W=59,F=21) is male/female
H=1.81
W=59
F=21
from scipy.stats import norm
score_M = pS0 * norm.pdf(H,mu_HS0,std_HS0) * norm.pdf(W,mu_WS0,std_WS0) * norm.pdf(F,mu_FS0,std_FS0)
score_F = pS1 * norm.pdf(H,mu_HS1,std_HS1) * norm.pdf(W,mu_WS1,std_WS1) * norm.pdf(F,mu_FS1,std_FS1)
print("score male    :", score_M)
print("score female  :", score_F)
print("proba male    :", score_M/(score_M+score_F))
print("proba female  :", score_F/(score_M+score_F))
