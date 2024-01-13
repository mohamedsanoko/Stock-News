import os
import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
ALPHA_API_KEY = os.environ.get("ALPHA_API_KEY")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILI0_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
alpha_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "IBM",
    "apikey": ALPHA_API_KEY
}
alpha_response = requests.get("https://www.alphavantage.co/query", params=alpha_parameters)
alpha_response.raise_for_status()
stocks_data = alpha_response.json()
print(stocks_data)
daily_stocks_data = stocks_data['Time Series (Daily)']
yesterday_stocks_tuple = list(daily_stocks_data.items())[0]
yesterday_date = yesterday_stocks_tuple[0]
day_before_yesterday_stocks_tuple = list(daily_stocks_data.items())[1]
yesterday_stock = yesterday_stocks_tuple[1]
day_before_yesterday_stock = day_before_yesterday_stocks_tuple[1]
yesterday_stock_price = float(yesterday_stock['4. close'])
day_before_yesterday_stock_price = float(day_before_yesterday_stock['4. close'])
percentage_change = (abs(yesterday_stock_price - day_before_yesterday_stock_price)/day_before_yesterday_stock_price) * 100
if percentage_change >= 5:
    print("Get News")
    news_params = {
        "q": "tesla",
        "from": yesterday_date,
        "sortBy": "publishedAt",
        "apiKey": NEWS_API_KEY
    }
    news_response = requests.get("https://newsapi.org/v2/everything", params=news_params)
    news_response.raise_for_status()
    news_data = news_response.json()
    first_three_news = news_data['articles'][0:3]
    first_three_news_description_list = []
    first_three_news_title_list = []
    for new in first_three_news:
        first_three_news_description_list.append(new['description'])
        first_three_news_title_list.append(new['title'])
    print(first_three_news_description_list)
    print(first_three_news_title_list)
    client = Client(TWILIO_ACCOUNT_SID, TWILI0_AUTH_TOKEN)
    if yesterday_stock_price > day_before_yesterday_stock_price:
        up_down_sign = "🔺"
    else:
        up_down_sign = "🔻"
    message_1 = f"TSLA: {up_down_sign}{round(percentage_change)}%\nHeadline: {first_three_news_title_list[0]}\nBrief: {first_three_news_description_list[0]}"
    message_2 = f"TSLA: {up_down_sign}{round(percentage_change)}%\nHeadline: {first_three_news_title_list[1]}\nBrief: {first_three_news_description_list[1]}"
    message_3 = f"TSLA: {up_down_sign}{round(percentage_change)}%\nHeadline: {first_three_news_title_list[2]}\nBrief: {first_three_news_description_list[2]}"

    message = client.messages.create(
            body=f"{message_1}",
            from_="+15412486181",
            to="+14383345118"
        )
    print(message.status)
    message = client.messages.create(
        body=f"{message_2}",
        from_="+15412486181",
        to="+14383345118"
    )
    print(message.status)
    message = client.messages.create(
        body=f"{message_3}",
        from_="+15412486181",
        to="+14383345118"
    )
    print(message.status)



## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

