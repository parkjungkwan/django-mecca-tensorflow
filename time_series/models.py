import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")
import pandas as pd
import pandas_datareader.data as web
import numpy as np
from icecream import ic
import matplotlib.pyplot as plt
from fbprophet import Prophet
from datetime import datetime
from pandas_datareader import data
import yfinance as yf
yf.pdr_override()
path = "c:/Windows/Fonts/malgun.ttf"
import platform
from matplotlib import font_manager, rc
if platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
else:
    print('Unknown system... sorry~~~~')
plt.rcParams['axes.unicode_minus'] = False
'''
시계열 데이터 
: 일련의 순차적으로 정해진 데이터 셋의 집합
: 시간에 관해 순서가 매겨져 있다는 점과, 연속한 관측치는 서로 상관관계를 갖고 있다
회귀분석
: 관찰된 연속형 변수들에 대해 두 변수 사이의 모형을 구한뒤 적합도를 측정해 내는 분석 방법
'''

class Model(object):

    def seasonal(self):
        start_date = '2018-1-4'
        end_date = '2021-6-30'
        KIA = data.get_data_yahoo('000270.KS', start_date, end_date)
        # ic(KIA.head())
        # ic(KIA.tail())

        KIA['Close'].plot(figsize=(12,6),grid=True)

        # 일부데이터로 forecast

        KIA_trunc = KIA[:'2021-12-31']
        df = pd.DataFrame({'ds': KIA_trunc.index,'y': KIA_trunc['Close']})
        df.reset_index(inplace=True)
        del df['Date']

        ic(df.head())

        m = Prophet(daily_seasonality=True)
        m.fit(df)
        future = m.make_future_dataframe(periods=61)
        future.tail()
        forecast = m.predict(future)

        m.plot(forecast)
        plt.figure(figsize=(12,6))
        plt.plot(KIA.index, KIA['Close'], label='real')
        plt.plot(forecast['ds'], forecast['yhat'], label='forecast')
        plt.grid()
        plt.legend()
        plt.show()



if __name__ == '__main__':
    m = Model()
    m.seasonal()