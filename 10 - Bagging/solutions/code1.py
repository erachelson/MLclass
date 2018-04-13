### WRITE YOUR CODE HERE
# If you get stuck, uncomment the line above to load a correction in this cell (then you can execute this code).

nb_samples = 100000
means = np.zeros((nb_samples,))
medians = np.zeros((nb_samples,))
for b in range(nb_samples):
    times_boot = np.random.choice(times, size=times.shape, replace=True)
    means[b]=np.mean(times_boot)
    medians[b]=np.median(times_boot)

count_mean,val_mean,_ = plt.hist(means, bins=np.arange(np.min(means),np.max(means),0.1))
plt.title("Bootstrap distribution of mean travel times")
plt.show()
count_median,val_median,_ = plt.hist(medians, bins=np.arange(np.min(medians),np.max(medians),0.5))
plt.title("Bootstrap distribution of median travel times")
plt.show()
print("Mean from the mean travel times histogram:", np.dot(count_mean,val_mean[:-1]) / np.sum(count_mean))
print("Empirical average of the mean travel times bootstrap samples:", np.mean(means))
print("Median from the median travel times histogram:", np.dot(count_median,val_median[:-1]) / np.sum(count_median))
print("Average median from the median travel times bootstrap samples:", np.mean(medians))
