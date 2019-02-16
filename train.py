import numpy as np
import torch
import torch.nn as nn
import torchvision
import torchvision.transforms as transforms
import cv2
from sklearn.model_selection import train_test_split

seed = 0
np.random.seed(seed)
torch.manual_seed(seed)

device = torch.device('cpu') # sad reax only

num_epochs = 10
num_classes = 9
batch_size = 64
learning_rate = 0.002

X = [] # image data, start as list
y = [] # output class data, start as list

for folder in os.listdir("./pictures/"):
    for file in os.listdir("./pictures/" + folder + "/"):
        im = cv2.imread("./pictures/" + folder + "/" + file)
        X.append(im)
        y.append(int(folder))

X = np.array(X)
y = np.array(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state = 0)

class ConvNet(nn.Module):
    def __init__(self, num_classes=num_classes):
        super(ConvNet, self).__init__()
        self.layer1 = nn.Sequential(
                nn.Conv2d(1, 16, kernel_size=5, stride=1, padding=2),
                nn.BatchNorm2d(16),
                nn.ReLU(),
                nn.maxPool2d(kernel_size=2, stride=2))
        self.layer2 = nn.Sequential(
                nn.Conv2d(16, 32, kernel_size=5, stride=1, padding=2),
                nn.BatchNorm(32),
                nn.ReLU(),
                nn.MaxPool2d(kernel_size=2, stride=2))
        self.fc = nn.Linear(7*7*32, num_classes)

    def forward(self, x):
        out = self.layer1(x)
        out = self.layer2(out)
        out = out.reshape(out.size(0), -1)
        out = self.fc(out)
        return out

