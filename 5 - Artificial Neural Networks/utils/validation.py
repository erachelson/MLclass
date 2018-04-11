import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score

def validation_report(test_data=None,
                      test_label=None,
                      model=None,
                      names=None):


    predictions = model.predict(test_data).argmax(axis=1)

    print("Accuracy: ")

    print(accuracy_score(predictions, test_label))

    print("\n\n")

    print("Confusion matrix: ")

    print(confusion_matrix(predictions, test_label))

    print("\n\n")

    print(classification_report(predictions, test_label, target_names=names))