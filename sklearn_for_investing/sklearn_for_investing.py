"""
DOCSTRING
"""
import datetime
import os
import time
import pandas
import sklearn
from matplotlib import pyplot

def introduction():
    """
    DOCSTRING
    """
    dataset = sklearn.datasets.load_digits(return_X_y=True)
    classifier = sklearn.svm.SVC(gamma=0.001, C=100)
    variable_x = dataset.data[:-1]
    variable_y = dataset.target[:-1]
    classifier.fit(variable_x, variable_y)
    prediction = classifier.predict(dataset.data[-1])
    print('Prediction:', prediction)
    pyplot.imshow(dataset.images[-1], cmap=pyplot.get_cmap('gray'), interpoation='nearest')
    pyplot.show()

def key_statistics(gather='Total Debt/Equity (mrq)'):
    """
    DOCSTRING
    """
    statistics_path = 'intraQuarter/_KeyStats'
    stock_list = [x[0] for x in os.walk(statistics_path)]
    for directory in stock_list[1:]:
        files = os.listdir(directory)
        ticker = directory.split('\\')[1]
        if len(files) > 0:
            for file in files:
                datestamp = datetime.datetime.strptime(file, '%Y%m%d%H%M%S.html')
                unix_time = time.mktime(datestamp.timetuple())
                full_filepath = os.path.join(directory, file)
                source = open(full_filepath, 'r').read()
                value = source.split(gather+':</td><td class="yfnc_tabledata1">')[1]
                value = value.split('</td>')[0]
                print(ticker + ':', value)
            time.sleep(15)

if __name__ == '__main__':
    key_statistics()