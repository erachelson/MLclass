class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(784, 120)
        self.fc3 = nn.Linear(120, 10)

    def forward(self, x):
        x = x.view(-1, 784)
        x = F.relu(self.fc1(x))
        x = self.fc3(x)
        return x

net = Net()
train(net)
y_test, predictions = get_test_predictions(net)
print("Accuracy: ")
print(accuracy_score(predictions, y_test))
print(classification_report(predictions, y_test, target_names=labels_text))
