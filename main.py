import os
os.system('pip install webdriver-manager')

from flask import Flask, render_template, jsonify
from crawl_stock import get_today_price, get_daily_stock_prices
from crawl_news import get_news_list
from crawl_bitcoin import get_bitcoin_price
from crawl_us_stock import get_us_stock_price
from crawl_weather import get_weather_info
import requests

from project2 import get_koreanexim_exchange_rate,get_naver_news_data,crawl_kospi_data,crawl_kosdaq_data
import json

from webdriver_manager.chrome import ChromeDriverManager

app = Flask(__name__,
            static_url_path='',
            static_folder='static',
            template_folder='templates'
            )


@app.route('/')
def project2():
    koreanexim_exchange_rate = get_koreanexim_exchange_rate()
    naver_news_data = json.loads(get_naver_news_data())

    news_title = "달러"
    news_list = get_news_list(news_title)
    print(news_list)

    # kospi = crawl_kospi_data()

    return render_template('project2.html',
                           koreanexim_exchange_rate=koreanexim_exchange_rate,
                           naver_news_data=naver_news_data,
                           news_title=news_title,
                           news_list=news_list)


@app.route('/kospi')
def get_kospi_data():
    kospi = crawl_kospi_data()
    print("done")
    print(kospi["day"])
    print(kospi["value"])
    return [kospi["day"],kospi["value"]]

@app.route('/kosdaq')
def get_kosdaq_data():
    kosdaq = crawl_kosdaq_data()
    print("done")
    print(kosdaq["day"])
    print(kosdaq["value"])
    return [kosdaq["day"],kosdaq["value"]]

@app.route('/dashboard')
def dashboard():
    # hyundai_price = get_today_price('005380')
    hyundai_price = 100000
    company1_stock = {'title': "현대자동차", "today_price": hyundai_price}
    company1_news_list = get_news_list("현대자동차")

    # shinsegae_price = get_today_price('004170')
    shinsegae_price = 70000
    company2_stock = {'title': "신세계", "today_price": shinsegae_price}
    company2_news_list = get_news_list("신세계")

    # us_stock_price = {'title': "tesla", 'today_price': get_us_stock_price('tesla')}
    us_stock_price = {'title': "tesla", 'today_price': 300000}
    bitcoin_price = get_bitcoin_price()

    weather_info = get_weather_info()

    return render_template('index.html',
                           company1_stock=company1_stock,
                           company1_news_list=company1_news_list,
                           company2_stock=company2_stock,
                           company2_news_list=company2_news_list,
                           us_stock_price=us_stock_price,
                           bitcoin_price=bitcoin_price,
                           weather_info=weather_info
                           )


@app.route('/weather_forecast')
def get_weather_forecast_info():
    result = requests.get('https://api.openweathermap.org/data/2.5/onecall?lat=37.413294&lon=126.734086&exclude=current,minutely,hourly,alerts&appid=3c9021aa10b48b8251d6555460a9f989&units=metric')
    json_result = result.json()
    print(type(json_result))
    print(type(json_result['daily']))
    return jsonify(json_result['daily'])


@app.route('/daily_prices')
def get_daily_prices():
    daily_price_list = get_daily_stock_prices()
    print(type(daily_price_list))
    return jsonify(daily_price_list)


@app.route('/line')
def get_line_chart_data():
    return jsonify(['data1', 30, 200, 100, 400, 150, 250])


@app.route('/pie')
def get_pie_chart_data():
    return jsonify([['A', 30], ['B', 50], ['C', 20]])


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)
