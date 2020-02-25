"""
DOCSTRING
"""
import datetime
import matplotlib.pyplot as pyplot
import matplotlib.style as style
import os
import pandas
import sklearn
import time

style.use('dark_background')

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
    pyplot.imshow(dataset.images[-1],
                  cmap=pyplot.get_cmap('gray'),
                  interpoation='nearest')
    pyplot.show()

def key_statistics(gather='Total Debt/Equity (mrq)'):
    """
    DOCSTRING
    """
    statistics_path = 'intraQuarter/_KeyStats'
    stock_list = [x[0] for x in os.walk(statistics_path)]
    dataframe_a = pandas.DataFrame(columns=['date',
                                            'unix',
                                            'ticker',
                                            'debt_to_equity',
                                            'price',
                                            'stock_change',
                                            'sp500',
                                            'sp500_change',
                                            'difference'])
    dataframe_sp500 = pandas.DataFrame.from_csv('data.csv')
    ticker_list = []
    for directory in stock_list[1:5]:
        files = os.listdir(directory)
        ticker = directory.split('\\')[1]
        ticker_list.append(ticker)
        initial_stock_value = False
        initial_sp500_value = False
        if len(files) > 0:
            for file in files:
                datestamp = datetime.datetime.strptime(file, '%Y%m%d%H%M%S.html')
                unix_time = time.mktime(datestamp.timetuple())
                full_filepath = os.path.join(directory, file)
                source = open(full_filepath, 'r').read()
                try:
                    value = source.split(gather+':</td><td class="yfnc_tabledata1">')[1]
                    value = float(value.split('</td>')[0])
                    try:
                        sp500_date = datetime.datetime.fromtimestamp(
                            unix_time).strftime('%Y-%m-%d')
                        row = dataframe_sp500[(dataframe_sp500.index == sp500_date)]
                        sp500_value = float(row['Adjusted Close'])
                    except:
                        sp500_date = datetime.datetime.fromtimestamp(
                            unix_time-259200).strftime('%Y-%m-%d')
                        row = dataframe_sp500[(dataframe_sp500.index == sp500_date)]
                        sp500_value = float(row['Adjusted Close'])
                    stock_price = float(
                        source.split('</small><big><b>')[1].split('</b></big>')[0])
                    if not initial_stock_value:
                        initial_stock_value = stock_price
                    if not initial_sp500_value:
                        initial_sp500_value = sp500_value
                    stock_change = ((stock_price-initial_stock_value)/initial_stock_valeu)*100
                    sp500_change = ((sp500_value-initial_sp500_value)/initial_sp500_value)*100
                    dataframe_a = dataframe_a.append({'date':datestamp,
                                                      'unix':unix_time,
                                                      'ticker':ticker,
                                                      'debt_to_equity':value,
                                                      'price':stock_price,
                                                      'stock_change':stock_change,
                                                      'sp500':sp500_value,
                                                      'sp500_change':sp500_change,
                                                      'difference':stock_change-sp500_change},
                                                     ignore_index=True)
                except:
                    pass
    for element in ticker_list:
        try:
            dataframe_plot = dataframe_a[dataframe_a['ticker'] == element]
            dataframe_plot = dataframe_plot.set_index(['date'])
            dataframe_plot['difference'].plot(label=element)
            pyplot.legend()
        except:
            pass
    pyplot.show()
    dataframe_a.to_csv(
        gather.replace(' ', '').replace('(', '').replace(')', '').replace('/', '') + '.csv')

if __name__ == '__main__':
    key_statistics()
