"""
DOCSTRING
"""
import datetime
import matplotlib.pyplot as pyplot
import matplotlib.style as style
import numpy
import os
import pandas
import sklearn.datasets as datasets
import sklearn.svm as svm
import time

def analysis():
    """
    DOCSTRING
    """
    variable_x, variable_y = build_data_set()
    classifier = svm.SVC(kernel='Linear', C=1.0)
    classifier.fit(variable_x, variable_y)
    #variable_w = classifier.coef_[0]
    #variable_a = -variable_w[0]/variable_w[1]
    #variable_xx = numpy.linspace(min(variable_x[:, 0]), max(variable_x[:, 0]))
    #variable_yy = (variable_a*variable_xx-classifier.intercept_[0])/variable_w[1]
    #variable_h0 = pyplot.plot(variable_xx, variable_yy, 'k-', label='Non-Weighted')
    pyplot.scatter(variable_x[:, 0], variable_x[:, 1], c=variable_y)
    pyplot.xlabel('DE Ratio')
    pyplot.ylabel('Trailing P/E')
    pyplot.legend()
    pyplot.show()

def build_data_set(features=['DE Ratio', 'Trailing P/E']):
    """
    DOCSTRING
    """
    dataframe_a = pandas.DataFrame.from_csv('data.csv')
    variable_x = numpy.array(dataframe_a[features].values)
    variable_y = (dataframe_a['Underperformed']
                  .replace(True, 0)
                  .replace(False, 1)
                  .valuse.to_list())
    return variable_x, variable_y

def introduction():
    """
    DOCSTRING
    """
    dataset = datasets.load_digits(return_X_y=True)
    classifier = svm.SVC(gamma=0.001, C=100)
    variable_x = dataset.data[:-1]
    variable_y = dataset.target[:-1]
    classifier.fit(variable_x, variable_y)
    prediction = classifier.predict(dataset.data[-1])
    print('Prediction:', prediction)
    pyplot.imshow(dataset.images[-1],
                  cmap=pyplot.get_cmap('gray'),
                  interpoation='nearest')
    pyplot.show()

def key_statistics(gather=['Beta',
                           'Book Value Per Share',
                           'Cash Flow',
                           'Current Ratio',
                           'Diluted EPS',
                           'Earnings Growth',
                           'EBITDA',
                           'Enterprise Value',
                           'Enterprise Value/EBITDA',
                           'Enterprise Value/Revenue',
                           'Forward P/E',
                           'Gross Profit',
                           'Held by Insiders',
                           'Held by Institutions',
                           'Market Cap',
                           'Net Income Avl to Common ',
                           'Operating Margin',
                           'PEG Ratio',
                           'Price/Book',
                           'Price/Sales',
                           'Profit Margin',
                           'Return on Assets',
                           'Return on Equity',
                           'Revenue',
                           'Revenue Growth',
                           'Revenue Per Share',
                           'Shares Short (as of',
                           'Shares Short (prior ',
                           'Short % of Float',
                           'Short Ratio',
                           'Total Cash',
                           'Total Cash Per Share',
                           'Total Debt',
                           'Total Debt/Equity (mrq)',
                           'Trailing P/E']):
    """
    DOCSTRING
    """
    style.use('dark_background')
    statistics_path = 'intraQuarter/_KeyStats'
    stock_list = [x[0] for x in os.walk(statistics_path)]
    dataframe_a = pandas.DataFrame(columns=['Beta',
                                            'Book Value Per Share',
                                            'Cash Flow',
                                            'Date',
                                            'DE Ratio',
                                            'Difference',
                                            'Diluted EPS',
                                            'Earnings Growth',
                                            'Current Ratio',
                                            'EBITDA',
                                            'Enterprise Value',
                                            'Enterprise Value/EBITDA',
                                            'Enterprise Value/Revenue',
                                            'Forward P/E',
                                            'Gross Profit',
                                            'Held by Insiders',
                                            'Held by Institutions',
                                            'Market Cap',
                                            'Net Income Avl to Common ',
                                            'Operating Margin',
                                            'PEG Ratio',
                                            'Price',
                                            'Price/Book',
                                            'Price/Sales',
                                            'Profit Margin',
                                            'Return on Assets',
                                            'Return on Equity',
                                            'Revenue',
                                            'Revenue Growth',
                                            'Revenue Per Share',
                                            'Shares Short (as of',
                                            'Shares Short (prior ',
                                            'Short % of Float',
                                            'Short Ratio',
                                            'SP500',
                                            'SP500_change',
                                            'Stock_change',
                                            'Ticker',
                                            'Total Cash',
                                            'Total Cash Per Share',
                                            'Total Debt',
                                            'Trailing P/E',
                                            'Underperformed',
                                            'Unix'])
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
                    for _ in gather:
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
                    difference = stock_change-sp500_change
                    if difference > 0:
                        underperformed = False
                    else:
                        underperformed = True
                    dataframe_a = dataframe_a.append({'date':datestamp,
                                                      'debt_to_equity':value,
                                                      'difference':difference,
                                                      'price':stock_price,
                                                      'sp500':sp500_value,
                                                      'sp500_change':sp500_change,
                                                      'stock_change':stock_change,
                                                      'ticker':ticker,
                                                      'underperformed':underperformed,
                                                      'unix':unix_time},
                                                     ignore_index=True)
                except:
                    pass
    for element in ticker_list:
        try:
            dataframe_plot = dataframe_a[dataframe_a['ticker'] == element]
            dataframe_plot = dataframe_plot.set_index(['date'])
            if dataframe_plot['underperformed'][-1]:
                color = 'r'
            else:
                color = 'g'
            dataframe_plot['difference'].plot(label=element, color=color)
            pyplot.legend()
        except:
            pass
    pyplot.show()
    dataframe_a.to_csv(
        gather.replace(' ', '').replace('(', '').replace(')', '').replace('/', '') + '.csv')

def support_vector_machine():
    """
    DOCSTRING
    """
    style.use('ggplot')
    variable_x = [1, 5, 1.5, 8, 1, 9]
    variable_y = [2, 8, 1.8, 8, 0.6, 11]
    pyplot.scatter(variable_x, variable_y)
    pyplot.show()
    variable_z = numpy.array([[1, 2], [5, 8], [1.5, 1.8], [8, 8], [1, 0.6], [9, 11]])
    variable_y = [0, 1, 0, 1, 0, 1]
    classifier = svm.SVC(kernel='linear', C=1.0)
    classifier.fit(variable_z, variable_y)
    print(classifier.predict([[0.58, 0.76]]))
    #variable_w = classifier.coef_[0]
    #variable_a = -variable_w[0]/variable_w[1]
    #variable_xx = numpy.linspace(0, 12)
    #variable_yy = (variable_a*variable_xx-classifier.intercept_[0])/variable_w[1]
    #variable_h0 = pyplot.plot(variable_xx, variable_yy, 'k-', label='Non-Weighted Division')
    pyplot.scatter(variable_z[:, 0], variable_z[:, 1], c=variable_y)
    pyplot.legend()
    pyplot.show()

if __name__ == '__main__':
    support_vector_machine()
