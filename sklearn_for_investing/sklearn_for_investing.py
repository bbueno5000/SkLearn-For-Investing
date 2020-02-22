"""
DOCSTRING
"""
from matplotlib import pyplot
from sklearn import datasets
from sklearn import svm

dataset = datasets.load_digits()
classifier = svm.SVC(gamma=0.001, C=100)
x = dataset.data[:-1]
y = dataset.target[:-1]
classifier.fit(x, y)
prediction = classifier.predict(dataset.data[-1])
print('Prediction:', prediction)
pyplot.imshow(dataset.images[-1], cmap=pyplot.cm_gray_r, interpoation='nearest')
pyplot.show()