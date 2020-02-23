"""
DOCSTRING
"""
import datetime
import os
import time
import pandas
import sklearn
import matplotlib.pyplot as pyplot

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
    pyplot.imshow(
        dataset.images[-1],
        cmap=pyplot.get_cmap('gray'),
        interpoation='nearest'
        )
    pyplot.show()

def key_statistics(gather='Total Debt/Equity (mrq)'):
    """
    DOCSTRING
    """
    statistics_path = 'intraQuarter/_KeyStats'
    stock_list = [x[0] for x in os.walk(statistics_path)]
    dataframe_a = pandas.DataFrame(columns=['date', 'unix', 'ticker', 'debt to equity'])
    for directory in stock_list[1:5]:
        files = os.listdir(directory)
        ticker = directory.split('\\')[1]
        if len(files) > 0:
            for file in files:
                datestamp = datetime.datetime.strptime(file, '%Y%m%d%H%M%S.html')
                unix_time = time.mktime(datestamp.timetuple())
                full_filepath = os.path.join(directory, file)
                source = open(full_filepath, 'r').read()
                try:
                    value = source.split(gather+':</td><td class="yfnc_tabledata1">')[1]
                    value = float(value.split('</td>')[0])
                    dataframe_a = dataframe_a.append(
                        {
                            'date':datestamp,
                            'unix':unix_time,
                            'ticker':ticker,
                            'debt to equity':value
                            },
                        ignore_index=True
                        )
                except:
                    pass
    dataframe_a.to_csv(
        gather.replace(' ', '').replace('(', '').replace(')', '').replace('/', '') + '.csv'
        )

if __name__ == '__main__':
    key_statistics()
