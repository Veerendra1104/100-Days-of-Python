import requests
from twilio.rest import Client

TWILIO_SSID = "Enter ssid"
TWILIO_API_KEY = "eneter epi key"
PHONE_NO = +14846635402
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

api = "https://www.alphavantage.co/query"

api_key = "enter api key"


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
parameters = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK,
    "apikey" : api_key,

}
response = requests.get(api, params=parameters)
data = response.json()['Time Series (Daily)']
# print(data)
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
# print(yesterday_data)
yesterday_closing_price = yesterday_data['4. close']
# print(yesterday_closing_price)


day_before_yesterday_data = data_list[1]
# print(yesterday_data)
day_before_yesterday_closing_price = day_before_yesterday_data['4. close']
# print(day_before_yesterday_closing_price)

difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
diff_percent = (difference / float(yesterday_closing_price))
difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
new_api_key = "9b192d7105704ab0b81bc87e3a245204"
news_api = "https://newsapi.org/v2/everything"

if abs(diff_percent) > 1 :
    parameters = {
        "q": STOCK,
        "apikey": new_api_key,
    }

    response = requests.get(news_api,params=parameters)
    articles = response.json()["articles"]

    three_articles = articles[:3]

    formatted_articles = [
        f"{STOCK}: {up_down}{diff_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for
        article in three_articles]
    # print(formatted_articles)

    ## STEP 3: Use https://www.twilio.com
    # Send a seperate message with the percentage change and each article's title and description to your phone number.
    client = Client(TWILIO_SSID, TWILIO_API_KEY)

    # TODO 8. - Send each article as a separate message via Twilio.
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_=PHONE_NO,
            to= +916362435914
        )

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

