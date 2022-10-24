from flask import Flask, request
from flask import render_template
import pandas as pd
import talib
from binance import Client

app = Flask(__name__)
key = 'wrfybb7xo2Cvze0Ii0zOO8FNkWIX4UCIWtBdONPZH7PD5nmP10pWVGDig9zFuffF'
secret = 'oPEp31iGEumVcl9NLcDTkwq3Q8F3A653ua2QYy33N1puebUsTbNdQo5gc8kP4UOR'

@app.route("/")
def hello_world():
    return ("Hello World")

@app.route("/mfi")
def mfi():
    args = request.args
    no1 = args['interval']
    no2 = args['coin']
    match interval:
        case "15m":
            data = client.get_historical_klines(coin, Client.KLINE_INTERVAL_15MINUTE,start_str = "1 days ago UTC")
        case "30m":
            data = client.get_historical_klines(coin, Client.KLINE_INTERVAL_30MINUTE,start_str = "2 days ago UTC")
        case "1h":
            data = client.get_historical_klines(coin, Client.KLINE_INTERVAL_1HOUR,start_str = "4 days ago UTC")
        case "4h":
            data = client.get_historical_klines(coin, Client.KLINE_INTERVAL_4HOUR,start_str = "16 days ago UTC")
        case "1d":
            data = client.get_historical_klines(coin, Client.KLINE_INTERVAL_1DAY,start_str = "96 days ago UTC")
    
    df = pd.DataFrame(data, columns=['date','open', 'high', 'low', 'close', 'volume','close_time', 'qav', 'num_trades',
                    'taker_base_vol', 'taker_quote_vol', 'ignore'])
    result = talib.MFI(df["high"], df["low"], df["close"], df["volume"], timeperiod=14)
    return f'no {no1} no2 {no2}'

@app.route("/b")
def b_world():
    key = 'wrfybb7xo2Cvze0Ii0zOO8FNkWIX4UCIWtBdONPZH7PD5nmP10pWVGDig9zFuffF'
    secret = 'oPEp31iGEumVcl9NLcDTkwq3Q8F3A653ua2QYy33N1puebUsTbNdQo5gc8kP4UOR'

    client = Client(api_key = key, api_secret = secret)

    data = client.get_historical_klines('BTCUSDT', Client.KLINE_INTERVAL_1MINUTE,start_str = "15 minutes ago UTC")
    #datah

    df = pd.DataFrame(data, columns=['date','open', 'high', 'low', 'close', 'volume','close_time', 'qav', 'num_trades',
                    'taker_base_vol', 'taker_quote_vol', 'ignore'])
    result = df['date'][0] + 5
    b= 10
    return f'a is {result} and b is {b}'

@app.route("/c")
def c_world():
    key = 'wrfybb7xo2Cvze0Ii0zOO8FNkWIX4UCIWtBdONPZH7PD5nmP10pWVGDig9zFuffF'
    secret = 'oPEp31iGEumVcl9NLcDTkwq3Q8F3A653ua2QYy33N1puebUsTbNdQo5gc8kP4UOR'

    client = Client(api_key = key, api_secret = secret)

    data = client.get_historical_klines('BTCUSDT', Client.KLINE_INTERVAL_1MINUTE,start_str = "15 minutes ago UTC")
    #datah

    df = pd.DataFrame(data, columns=['date','open', 'high', 'low', 'close', 'volume','close_time', 'qav', 'num_trades',
                    'taker_base_vol', 'taker_quote_vol', 'ignore'])
    print(df['date'][0] , " asd")
    return (df['date'][0] , " asd")

@app.route("/d")
def d_world():
    key = 'wrfybb7xo2Cvze0Ii0zOO8FNkWIX4UCIWtBdONPZH7PD5nmP10pWVGDig9zFuffF'
    secret = 'oPEp31iGEumVcl9NLcDTkwq3Q8F3A653ua2QYy33N1puebUsTbNdQo5gc8kP4UOR'

    client = Client(api_key = key, api_secret = secret)

    data = client.get_historical_klines('BTCUSDT', Client.KLINE_INTERVAL_1MINUTE,start_str = "15 minutes ago UTC")
    #datah

    df = pd.DataFrame(data, columns=['date','open', 'high', 'low', 'close', 'volume','close_time', 'qav', 'num_trades',
                    'taker_base_vol', 'taker_quote_vol', 'ignore'])
    print(df['date'][0] , " asd")
    return (" asd")