import yfinance as yf
import smtplib
from email.mime.text import MIMEText
import time
import json
import matplotlib.pyplot as plt
import requests

# 설정 파일 경로
SETTINGS_FILE = 'settings.json'

def load_settings():
    with open(SETTINGS_FILE, 'r') as file:
        return json.load(file)

def save_settings(settings):
    with open(SETTINGS_FILE, 'w') as file:
        json.dump(settings, file)

def send_email(subject, body, to_email):
    from_email = 'your_email@example.com'
    password = 'your_password'
    
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email
    
    with smtplib.SMTP('smtp.example.com', 587) as server:
        server.starttls()
        server.login(from_email, password)
        server.sendmail(from_email, to_email, msg.as_string())

def send_sms(body):
    account_sid = 'your_account_sid'
    auth_token = 'your_auth_token'
    from_phone = 'your_twilio_phone'
    to_phone = 'recipient_phone'
    
    from twilio.rest import Client
    client = Client(account_sid, auth_token)
    client.messages.create(body=body, from_=from_phone, to=to_phone)

def send_discord_message(webhook_url, message):
    data = {"content": message}
    requests.post(webhook_url, json=data)

def fetch_news(ticker):
    url = f'https://newsapi.org/v2/everything?q={ticker}&apiKey=your_news_api_key'
    response = requests.get(url)
    news_data = response.json()
    return news_data['articles']

def track_stocks(stock_list):
    prices = {ticker: [] for ticker in stock_list}
    
    while True:
        for ticker in stock_list:
            stock = yf.Ticker(ticker)
            current_price = stock.history(period='1d')['Close'][0]
            prices[ticker].append(current_price)
            print(f"{ticker} Current Price: ${current_price:.2f}")

            # 알림 조건 확인
            if current_price <= settings['target_prices'][ticker]:
                subject = f"{ticker} Alert!"
                body = f"The stock price of {ticker} has reached your target price.\nCurrent Price: ${current_price:.2f}"
                send_email(subject, body, settings['email'])
                send_sms(body)
                send_discord_message(settings['discord_webhook'], body)
                print("Alerts sent!")

            # 뉴스 가져오기
            news = fetch_news(ticker)
            if news:
                subject = f"{ticker} News Alert"
                body = "\n".join([f"{article['title']}" for article in news[:5]])
                send_email(subject, body, settings['email'])
                send_discord_message(settings['discord_webhook'], body)

        # 가격 시각화
        plot_prices(prices)

        time.sleep(settings['check_interval'])

def plot_prices(prices):
    plt.figure(figsize=(10, 5))
    for ticker, price_list in prices.items():
        plt.plot(price_list, label=ticker)
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.title('Stock Prices')
    plt.legend()
    plt.show()

# 사용자 설정 불러오기
settings = load_settings()

# 추적할 주식 리스트
track_stocks(settings['stock_list'])
