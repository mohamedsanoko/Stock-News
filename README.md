# Stock News Notifier
This Python script provides a stock news notifier that sends SMS alerts when the stock price of a specified company experiences a significant percentage change. It fetches stock price data from Alpha Vantage, news articles from the News API, and utilizes Twilio for sending SMS alerts.

# Getting Started
  1. Clone the Repository.
  2. Install Dependencies.
  3. Set Up Environment Variables for security.
  4. Run the Script.

# Project Structure
The project consists of a single Python script. This script fetches stock price data from Alpha Vantage, checks for a significant percentage change, fetches news articles using the News API, and sends SMS alerts using Twilio.

# How It Works
  1. The script uses Alpha Vantage to fetch daily stock price data for a specified stock symbol       ('STOCK'). It calculates the percentage change between yesterday's and the day before              yesterday's closing prices.
  2. If the percentage change is greater than or equal to 5%, the script uses the News API to         fetch the first three news articles related to the specified company (COMPANY_NAME).
  3. The Twilio client is initialized, and separate SMS alerts are sent for each news article,         including the percentage change and the article's title and description.

# Customization
**Stock and Company Information**: 
  1. Update 'STOCK' with the desired stock symbol.
  2. Update 'COMPANY_NAME' with the desired company name.
**Twilio SMS Alert**: Customize the SMS alert message format in the script to match your preferences.

# Notes
The script uses Alpha Vantage for stock price data and the News API for fetching news articles. Ensure that you have valid API keys for these services.

Twilio is used to send SMS alerts. Make sure to replace the Twilio account SID, authentication token, and phone numbers in the script.

The project includes placeholders for API keys and environment variables. Replace these placeholders with your actual API keys and details.
