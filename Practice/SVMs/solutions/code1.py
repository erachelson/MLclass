### WRITE YOUR CODE HERE
# If you get stuck, uncomment the line above to load a correction in this cell (then you can execute this code).

data_file = 'data/atheist.dat'
df = pd.read_csv(data_file, sep='\s+', header=None, names=['attendance', 'tolerance'])
print(df.shape)       # --> (nrow, ncols)
print(df.iloc[0:5,:]) # print first lines of dataset


