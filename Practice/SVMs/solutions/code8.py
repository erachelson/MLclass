### WRITE YOUR CODE HERE
# If you get stuck, uncomment the line above to load a correction in this cell (then you can execute this code).

# Read arff data
import pandas as pd
import scipy
from scipy.io import arff

# Load yeast.arff via dedicate scipy.io function
raw_data, metadata = arff.loadarff('data/yeast.arff')
print("nrows:", len(raw_data))    # 2417
print("ncols:", len(raw_data[0])) #  117

# Data to pandas, converting unicode columns to integers
df = pd.DataFrame(raw_data)
# print(df.shape)           # -> (2417, 117)
# print(df.head(5))         # for free, we get column names
# print(type(df.iloc[0,0])) # -> <class 'bytes'> ## we want to have plain {0,1} integers

classes_list = [name for name in df.columns if "Class" in name]
# print(classes_list)  # -> ['Class1', 'Class2', ... , 'Class14']

for col in df[classes_list]:
    df[col] = (df[col].str.decode('utf-8').astype(int))

print(type(df.iloc[0,0]))  # -> int: as expected
print(type(df.iloc[0,15])) # -> float: as expected
print("dataframe dimensions:", df.shape)    # -> (2417, 117)
