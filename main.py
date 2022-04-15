import mysql.connector

moneycontrol = mysql.connector.connect(host="localhost", user="root", password="Deva!@#$", database="moneycontrol")
cursor = moneycontrol.cursor()
#cursor.execute('Create Database moneycontrol')
cursor.execute("drop table data")
cursor.execute("CREATE TABLE data(ID INT, Name VARCHAR(500), Market_Price VARCHAR(100), Ref_Url VARCHAR(1000),Datetime VARCHAR(50))")

from bs4 import BeautifulSoup
import requests
from Urls.Urls import urls
import pandas as pd
import datetime

id = 0
data=[]
for links in urls:
    page = requests.get(links)
    soup = BeautifulSoup(page.text, 'lxml')
    date_time = datetime.datetime.now()
    try:
        name = soup.find('h1').text
        market_price = soup.find('div', class_='inprice1 nsecp').text
    except:
        market_price = ''
        name = ''
    id += 1

    print(id,name,market_price,links,date_time)
    extract = "insert into data(ID, Name, Market_Price, Ref_Url, Datetime)values(%s,%s,%s,%s,%s)"
    data_db=[id,name,market_price,links,date_time]
    cursor.execute(extract,data_db)
    moneycontrol.commit()
