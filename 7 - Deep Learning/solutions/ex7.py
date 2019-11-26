class DropoutNet(nn.Module):
    
    def __init__(self):
        super(DropoutNet, self).__init__()
        self.fc1 = nn.Linear(784,600)
        self.drop = nn.Dropout(0.25)
        self.fc2 = nn.Linear(600, 120)
        self.fc3 = nn.Linear(120, 10)
        
    def forward(self, x):
        x = x.view(-1,784)
        x = self.fc1(x)
        x = self.drop(x)
        x = self.fc2(x)
        x = self.fc3(x)
        return x
