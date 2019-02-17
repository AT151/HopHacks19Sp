import numpy as np
import torch
import torch.nn as nn
import torchvision
import torchvision.transforms as transforms
from torch.utils.data import Dataset, DataLoader
import torch.nn.functional as F
import torch.optim as optim
from torch.autograd import Variable
import cv2
from sklearn.model_selection import train_test_split
import os
import pickle

device = torch.device('cpu')  # sad reax only

x = []  # image data, start as list
y = []  # output class data, start as list

for folder in os.listdir("./pictures/"):
    for file in os.listdir("./pictures/" + folder + "/"):
        im = cv2.imread("./pictures/" + folder + "/" + file)
        im = np.reshape(im, (3, 256, 144))
        x.append(im)
        out = np.zeros(9)
        out[int(folder)] = 1
        # out = int(folder)
        y.append(out)

x = np.array(x)
y = np.array(y)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.002, random_state=0)


class TrainDataset(Dataset):
    def __init__(self):
        self.len = x_train.shape[0]
        self.x_data = torch.from_numpy(x_train).type(torch.FloatTensor)
        self.y_data = torch.from_numpy(y_train).type(torch.LongTensor)

    def __getitem__(self, index):
        return self.x_data[index], self.y_data[index]

    def __len__(self):
        return self.len


class TestDataset(Dataset):
    def __init__(self):
        self.len = x_test.shape[0]
        self.x_data = torch.from_numpy(x_test).type(torch.FloatTensor)
        self.y_data = torch.from_numpy(y_test).type(torch.LongTensor)

    def __getitem__(self, index):
        return self.x_data[index], self.y_data[index]

    def __len__(self):
        return self.len


class Net(nn.Module):
    def __init__(self, num_classes=9):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(3, 5, 5, 1)
        self.conv2 = nn.Conv2d(5, 10, 5, 1)
        self.fc1 = nn.Linear(20130, 10)
        self.fc2 = nn.Linear(10, num_classes)

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = F.max_pool2d(x, 2, 2)
        x = F.relu(self.conv2(x))
        x = F.max_pool2d(x, 2, 2)
        x = x.view(-1, 20130)
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return F.log_softmax(x, dim=1)


learning_rate = 0.002
model = Net()
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)
criterion = nn.CrossEntropyLoss()

def train(epoch, train_loader):
    model.train()
    for batch_idx, (data, target) in enumerate(train_loader):
        data, target = Variable(data), Variable(target)
        #print(data)
        #print(target)
        optimizer.zero_grad()
        output = model(data)
        loss = criterion(output, torch.max(target, 1)[1])
        loss.backward()
        optimizer.step()
        if batch_idx % 10 == 0:
            print('Train Epoch: {} [{}/{} ({:.0f}%)]\tLoss: {:.6f}'.format(
                epoch, batch_idx * len(data), len(train_loader.dataset),
                       100. * batch_idx / len(train_loader), loss.data))
    if epoch == 10:
        pkl_filename = "pickle_model.pkl"
        with open(pkl_filename, 'wb') as file:
            pickle.dump(model, file)


def test(test_loader):
    model.eval()
    test_loss = 0
    correct = 0
    for data, target in test_loader:
        data, target = Variable(data, volatile=True), Variable(target)
        output = model(data)
        # sum up batch loss
        test_loss += criterion(output, torch.max(target, 1)[1])
        # get the index of the max log-probability
        pred = output.data.max(1, keepdim=True)[1]
        correct += pred.eq(target.data.view_as(pred)).cpu().sum()

    test_loss /= len(test_loader.dataset)
    print('\nTest set: Average loss: {:.4f}, Accuracy: {}/{} ({:.0f}%)\n'.format(
        test_loss, correct, len(test_loader.dataset),
        100. * correct / len(test_loader.dataset)))


if __name__ == '__main__':
    train_dataset = TrainDataset()
    train_loader = DataLoader(dataset=train_dataset, batch_size=1, shuffle=True)

    test_dataset = TestDataset()
    test_loader = DataLoader(dataset=test_dataset, batch_size=1, shuffle=False)

    """for epoch in range(5):
        for i, data in enumerate(train_loader, 0):
            inputs, labels = data
            inputs, labels = Variable(inputs), Variable(labels)
            print(epoch, i, "inputs", inputs.data, "labels", labels.data)"""

    for epoch in range(1, 11):
        train(epoch, train_loader)

        # test(test_loader)

