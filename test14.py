import requests
import bs4
import urllib
from urllib.request import urlopen
import pymysql

#데이터 베이스 연결
conn = pymysql.connect(host ='127.0.0.1', user='root', password = '19992899', db='dw_501',charset='utf8')
#데이터베이스 연결 후에 커서 생성, 커서는 파이썬과 DB 사이를 연결해주는 드라이버의 형태
#커서생성
cur = conn.cursor()

# 쇼핑몰에서 이름 가져오기
url = "https://www.graychic.co.kr/product/list.html?cate_no=4"
#res = requests.get(url =url)
html = urlopen(url)

bsp = bs4.BeautifulSoup(html,"html.parser")
href_list= []
items = bsp.findAll("div",{"class","sp-product__thumb"})
for item in items:
    href_list.append( item.find("a")['href'])

site="https://www.graychic.co.kr"
#여기부터가 하나 인덱스 바꿔서 하면 됨 => 반복문 돌려야됨
#파이썬에서는 try-catch가 아니라 try-except가 예외처리문임
item_list = dict() # 제품의 상세 정보 저장 딕셔너리(key-상품명, value-정보)


for i in range(len(href_list)):
    href= urllib.parse.quote(href_list[i]) #한글을 인코딩
    item_link = site + href  #제품 상세페이지 주소

    item_html = urlopen(item_link)  # 제품 상세페이지 html

    item_bsp = bs4.BeautifulSoup(item_html,"html.parser") #제품상세페이지 파서


    item_name='' #제품명
    info_t = item_bsp.select_one("#gc_de_sizeinfo")

    info_tr = info_t.select("tr")
    th_list=[]  
    td_list=[]
    try:
        for tr in info_tr:
            try:
                th=tr.select_one("th").text
                td = tr.select_one("td").text
            except Exception as e:
                continue
            else:
                if '상품명'==th:
                    item_name=td
                else:
                    th_list.append(th)
                    td_list.append(td)
    except Exception as e:
        print("몇번 째 제품 오류 :"+ str(i))

    size_t = item_bsp.select_one("#gc_de_sizecm")
    size_th = size_t.select("th")
    for th in size_th:
        th_list.append(th.text)
    size_td = size_t.select("td")
    for td in size_td:
        td_list.append(td.text)

    item_list[item_name] = dict(zip(th_list,td_list))

db_column = ['색상','소재','모델착용','세탁팁','사이즈','어깨단면','어깨길이',
'소매길이','암홀','가슴단면','총기장','트임','소매트임']

for name in item_list:
    item_title = list(item_list[name].keys()) #딕셔너리의 키르르 리스트로 변환
    item_value=[] # 실제 상품의 정보값들을 저장할 리스트(DB저장용)
    i=0
    for col in db_column:
        if col in item_title[i]: #실제 상품정보의 명칭이 DB컬럼과 일치하면 값 저장
            item_value.append(item_list[name][item_title[i]])
            i+=1
        else: #실제 상품정보의 명칭이 DB컬럼과 일치하지 않으면 0저장
            item_value.append(0)
    cur.execute( "insert into outers(item_name,item_color,item_mat,item_modelwear,item_washing,item_size,item_shoulder,item_shoulder_len,item_sleeve,item_armhole,item_chest,item_len,item_open,item_opensleeve) values('{0}','{1}','{2}','{3}','{4}','{5}',{6},{7},{8},{9},{10},{11},{12},{13})".format(name,item_value[0],
    item_value[1],item_value[2],item_value[3],item_value[4],item_value[5],item_value[6],item_value[7],item_value[8],item_value[9],item_value[10],item_value[11],item_value[12]))
    conn.commit()
conn.close()

# print( item_list)


# find -> tag로 찾기, # select -> css 선택자로 찾기
# find -> 태그 1개찾기 # findAll -> 태그 여러개 
# select -> 선택자에 해당하는 모든 태그 # selectOne -> 1개 태그