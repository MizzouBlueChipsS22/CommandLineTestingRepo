#Ignore, keep here for references and backlog
"""import requests
from selenium import webdriver
from bs4 import BeautifulSoup


url = 'https://finviz.com/screener.ashx'

#Does not print correct HTML file for some reason, possible DDoS protection by Cloudflare
r = requests.get(url).text

data = BeautifulSoup(r, 'lxml')

print(data)

#Selenium usage, does nothing productive
browser = webdriver.Chrome()
data = browser.get(url)"""

#New Start
from finviz.screener import Screener
from finviz.portfolio import Portfolio

#gets stock tickers and saves into csv
stockList = Screener()
print(type(stockList))  #TESTING REFERENCE
stockList.to_csv('finviz.csv')

#portfolio data
