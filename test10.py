

# http - 하이퍼 텍스트(html)을 전송하기위한 프로토콜
# 프로토콜 - 약속 , 규약
# url - http://www.naver.com
# uri - url에 사용자 정보와 스키마를 포함한값

# 스크래핑 - 웹페이지에서 자동으로 데이터를 추출하는것 웹페이지 소유자의 허락없이 무단으로 끌어오는 행위
# 크롤링 - 웹페이지에서 자동으로 데이터 추출
# 스크래핑은 특정 웹사이트에서 데이터 추출, 크롤링은 웹사이트의 링크를통해서 정보를 찾아서 추출하는방식
# 둘다 데이터추출한다는것이 동일하기에 흔히 크롤링이라 한다.


from urllib.request import urlopen

# url = "https://www.naver.com"

# html = urlopen(url)

# print(html.read())
import bs4

html = """
  <html>
    <body>
      <div>
        <ul class='kjy'>
          <li>ljh</li>
          <li>jyj</li>
          <li>babo</li>
          <li>old....</li>
        </ul>
        <ul class='ljh'>
          <li>ljh</li>
          <li>jyj</li>
          <li>babo</li>
          <li>old....</li>
        </ul>
      </div>
    </body>
  </html>      
"""

# ul = bsp.find("ul",{"class":"ljh"})
# print(ul["class"])
# li = bsp.findAll("li")
# print(li)

url = "https://www.op.gg/statistics/champions"

html = urlopen(url)

html = html.read()

bsp = bs4.BeautifulSoup(html, "html.parser")
# temp = bsp.findAll("div",{"class","css-hkh81z"})

# op_div = bsp.findAll("table")

# print(op_div)















# chp = temp.find("div",{"class","css-qzg52u"})
# print(chp)
# temp = bsp.findAll("strong",{"class","current"})

# print(temp)
# for i in temp:
#   if "현재기온" in i:
#     print(i.text)
# # print(temp[0].text)


# temp = bsp.findAll("a",{"class","nav"})

# for i in temp:
#   print(i.text)


# ul = bsp.find("ul",{"class","type02"})
# li = ul.findAll("li")


# for tmp in li:
#   temp = tmp.find("strong")
#   print(temp.text)

# temp = bsp.find("div",{"class","col_selected"})
# thu = temp.findAll("li")
# for tmp in thu:

#   title = tmp.find("a",{"class","title"})
#   print(title.text)

