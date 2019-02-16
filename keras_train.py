import numpy as np
from keras import models, layers, regularizers, losses, optimizers, metrics
X = []  # image data, start as list
y = []  # output class data, start as list

for folder in os.listdir("./pictures/"):
    for file in os.listdir("./pictures/" + folder + "/"):
        im = cv2.imread("./pictures/" + folder + "/" + file)
        X.append(im)
        y.append(int(folder))

print(len(X))
print(len(y))
X = np.array(X)
print(X.shape)
X = np.resize(X, (4124, 3, 72, 128))
print(X.shape)
for i in range(4124):
    X[i] = np.reshape(X[i], (128, 72, 3))
y = np.array(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
print(X_train.shape)