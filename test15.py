import requests
import bs4
import urllib
from urllib.request import urlopen
import pymysql

url = "https://weather.naver.com/today/07140102?cpName=KMA"

html = urlopen(url)

bsp = bs4.BeautifulSoup(html,"html.parser")

# weather = bsp.find("div",{"id","hourly"})

w_div = bsp.findAll("div",{"class","weather_table_wrap"})
w_tr = w_div[0].findAll("tr",{"class","thead _cnTimeTable"})
w_time = []
w_name = []
dic = dict()

for tmp in w_div:
  t_span = w_tr[0].findAll("span",{"class","time"})
  n_span = w_tr[0].findAll("span",{"class","blind"})
  for temp in t_span:
    w_time.append(temp.text)
  for temp in n_span:  
    w_name.append(temp.text)
  dic = dict(zip(w_time,w_name))  
print(dic)

weather_div = w_div[0].find("table")
weather_tbody = weather_div.find("tbody")
weather_tr = weather_tbody.fianAll("tr")
for weather in weather_tr:
  print(weather.text)
