from flask import Flask
from flask import render_template
import pandas as pd
#import talib
from binance import Client

app = Flask(__name__)


@app.route("/")
def hello_world():
    return ("Hello World")

@app.route("/b")
def bye_world():
    # key = 'wrfybb7xo2Cvze0Ii0zOO8FNkWIX4UCIWtBdONPZH7PD5nmP10pWVGDig9zFuffF'
    # secret = 'oPEp31iGEumVcl9NLcDTkwq3Q8F3A653ua2QYy33N1puebUsTbNdQo5gc8kP4UOR'

    # client = Client(api_key = key, api_secret = secret)

    # data = client.get_historical_klines('BTCUSDT', Client.KLINE_INTERVAL_1MINUTE,start_str = "15 minutes ago UTC")
    # #datah

    # df = pd.DataFrame(data, columns=['date','open', 'high', 'low', 'close', 'volume','close_time', 'qav', 'num_trades',
    #                 'taker_base_vol', 'taker_quote_vol', 'ignore'])
    # return df
    return ("talib")
