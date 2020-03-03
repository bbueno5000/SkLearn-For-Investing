"""
DOCSTRING
"""
import datetime
import os
import time

import matplotlib.pyplot as pyplot
import matplotlib.style as style
import numpy
import pandas
import quandl
import sklearn.datasets as datasets
import sklearn.preprocessing as preprocessing
import sklearn.svm as svm

FEATURES = ['DE Ratio',
            'Trailing P/E',
            'Price/Sales',
            'Price/Book',
            'Profit Margin',
            'Operating Margin',
            'Return on Assets',
            'Return on Equity',
            'Revenue Per Share',
            'Market Cap',
            'Enterprise Value',
            'Forward P/E',
            'PEG Ratio',
            'Enterprise Value/Revenue',
            'Enterprise Value/EBITDA',
            'Revenue',
            'Gross Profit',
            'EBITDA',
            'Net Income Avl to Common ',
            'Diluted EPS',
            'Earnings Growth',
            'Revenue Growth',
            'Total Cash',
            'Total Cash Per Share',
            'Total Debt',
            'Current Ratio',
            'Book Value Per Share',
            'Cash Flow',
            'Beta',
            'Held by Insiders',
            'Held by Institutions',
            'Shares Short (as of',
            'Short Ratio',
            'Short % of Float',
            'Shares Short (prior ']

class SklearnInvesting():
    """
    DOCSTRING
    """
    def analysis(self):
        """
        DOCSTRING
        """
        test_size = 500
        variable_x, variable_y = self.build_data_set()
        classifier = svm.SVC(kernel='Linear', C=1.0)
        classifier.fit(variable_x[:-test_size], variable_y[:-test_size])
        correct_count = 0
        for count in range(1, test_size+1):
            if classifier.predict(variable_x[-count])[0] == variable_y[-count]:
                correct_count += 1
        print('Accuracy:', (correct_count/test_size)*100.00)

    def build_data_set(self):
        """
        DOCSTRING
        """
        dataframe_a = pandas.DataFrame.from_csv('data.csv')
        dataframe_a = dataframe_a.reindex(numpy.random.permutation(dataframe_a.index))
        variable_x = numpy.array(dataframe_a[FEATURES].values)
        variable_y = (dataframe_a['Underperformed']
                      .replace(True, 0)
                      .replace(False, 1)
                      .valuse.to_list())
        variable_x = preprocessing.scale(variable_x)
        return variable_x, variable_y

    def introduction(self):
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

    def key_statistics(self, gather=['Beta',
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

    def randomizing(self):
        """
        DOCSTRING
        """
        dataframe_a = pandas.DataFrame({'D1':range(5), 'D2':range(5)})
        dataframe_b = dataframe_a.reindex(numpy.random.permutation(dataframe_a.index))

    def stock_prices(self):
        """
        DOCSTRING
        """
        string_a = open('auth.txt', 'r').read()
        string_b = 'intraQuarter/_KeyStats'
        list_a = [x[0] for x in os.walk(string_b)]
        dataframe_a = pandas.DataFrame()
        for element in list_a[1:]:
            string_c = element.split('\\')[1]
            string_d = 'WIKI/' + string_c.upper()
            dataframe_b = quandl.get(
                string_d,
                trim_start='2000-12-12',
                trim_end='2014-12-30',
                auth_token=string_a)
            dataframe_b[string_c.upper()] = dataframe_b['Adj. Close']
            dataframe_a = pandas.concat([dataframe_a, dataframe_b['ticker.upper()']], axis=1)
        dataframe_a.to_csv('stock_prices.csv')

    def support_vector_machine(self):
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
    SklearnInvesting().support_vector_machine()
