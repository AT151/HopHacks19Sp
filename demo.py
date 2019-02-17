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

model = pickle.load(open("pickle_model.pkl"))
while True:
    for file in os.listdir("../../../../Downloads/"):
        l = []
        if 'downlo' in file:
            print("hello")