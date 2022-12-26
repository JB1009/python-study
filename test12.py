import requests
import bs4
import urllib
from urllib.request import urlopen
import pymysql
# from urllib.parse import urlparse

conn = pymysql.connect(host='127.0.0.1',user="root",password="19992899",db="dw_501",charset="utf8")
url = "https://www.graychic.co.kr/product/list.html?cate_no=4"
cur = conn.cursor()
html = urlopen(url)
bsp = bs4.BeautifulSoup(html, "html.parser")

items = bsp.findAll("div", {"class", "sp-product__thumb"})
href_list = []

for i in items:
    href_list.append(i.find("a")["href"])

# print(href_list)

site = "https://www.graychic.co.kr"
item_list = dict()
for i in range(len(href_list)):
    href = urllib.parse.quote(href_list[i])
    item_link = site + href

    item_html = urlopen(item_link)

    item_bsp = bs4.BeautifulSoup(item_html, "html.parser")

    item_name = ""
    info_t = item_bsp.select_one("#gc_de_sizeinfo")

    info_tr = info_t.select('tr')
    th_list = []
    td_list = []

    # 상품정보
    try:
        for tr in info_tr:
          try:
            th = tr.select_one("th").text
            td = tr.select_one("td").text
          except Exception as e : 
            continue
          else:
            if "상품명" == th:
              item_name = td
            else:
              th_list.append(th)
              td_list.append(td)
       
        # 사이즈
    except Exception as e:
        print("몇번째 제품오류 : " + str(i))

    size_t = item_bsp.select_one("#gc_de_sizecm")
    size_th = size_t.select("th")
    for th in size_th:
        th_list.append(th.text)
    size_td = size_t.select("td")
    for td in size_td:
        td_list.append(td.text)

    item_list[item_name] = dict(zip(th_list, td_list))
print(item_list)
# cur.execute("insert into outers values('"+item_list[item_name][0]+"')")

# info_tbody = info_t.find("tbody")
# info_tr = info_t.findAll("tr")

# for tr in info_tr:
#   th = tr.find("th").text
#   td = th.find("td").text
#   print(th,td)
# print(info_t)

# names = bsp.findAll("p",{"class","name"})
# price = bsp.findAll("span",{"class","p_value"})

# info = []

# for tmp in range(len(names)):
#   name = names[tmp].find("a").text
#   p = price[tmp].find("strong").text
#   info.append([name,p])
# print(info)
