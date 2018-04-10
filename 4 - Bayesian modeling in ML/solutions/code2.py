### WRITE YOUR CODE HERE
# If you get stuck, uncomment the line above to load a correction in this cell (then you can execute this code).

log_score_M = np.log(pS0) + norm.logpdf(H,mu_HS0,std_HS0) + norm.logpdf(W,mu_WS0,std_WS0) + norm.logpdf(F,mu_FS0,std_FS0)
log_score_F = np.log(pS1) + norm.logpdf(H,mu_HS1,std_HS1) + norm.logpdf(W,mu_WS1,std_WS1) + norm.logpdf(F,mu_FS1,std_FS1)
print("log score male:    ", log_score_M)
print("log score female:  ", log_score_F)
