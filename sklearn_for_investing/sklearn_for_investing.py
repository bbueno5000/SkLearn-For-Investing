"""
DOCSTRING
"""
import datetime
import os
import time
import pandas
from matplotlib import pyplot
from sklearn import datasets
from sklearn import svm

def introduction():
    """
    DOCSTRING
    """
    dataset = datasets.load_digits()
    classifier = svm.SVC(gamma=0.001, C=100)
    variable_x = dataset.data[:-1]
    variable_y = dataset.target[:-1]
    classifier.fit(variable_x, variable_y)
    prediction = classifier.predict(dataset.data[-1])
    print('Prediction:', prediction)
    pyplot.imshow(dataset.images[-1], cmap=pyplot.cm_gray_r, interpoation='nearest')
    pyplot.show()

def key_statistics(gather='Total Debt/Equity (mrq)'):
    """
    DOCSTRING
    """
    filepath = 'intraQuarter'
    statistics_path = os.path.join(filepath, ' KeyStats')
    stock_list = [x[0] for x in os.walk(statistics_path)]
    for directory in stock_list[1:]:
        files = os.listdir(directory)
        if len(files) > 0:
            for file in files:
                datestamp = datetime.strptime(file, '%Y%m&d%H%M%S.html')
                unix_time = time.mktime(datestamp.timetuple())
