### WRITE YOUR CODE HERE
# If you get stuck, uncomment the line above to load a correction in this cell (then you can execute this code).

# === Hints:
CVRATIO = 0.4

# === Solution:
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split

# Get a list of all features: "Att1" ... "Att103"
features_list = [name for name in df.columns if "Att" in name]

# Shuffle rows
df = df.sample(frac=1)

# Shown classifier n.1. To you to put it in a nice for loop and store the results
X_train, X_test, y_train, y_test = train_test_split(
    df[features_list],
    df[classes_list],
    test_size=0.4,
    random_state=0 # <- random seed, could be useful to replicate previous results
)

clf = SVC(gamma='auto')
clf.fit(X_train, y_train["Class1"])

y_pred_01 = clf.predict(X_test)

