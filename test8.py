# 함수
# 자바의 메서드
# 반환타입 메서드이름(매개변수){ 실행내용 반환타입이있다면 return ;}

# 자바스크립트 함수
# function 함수이름(매개변수){ 실행내용 }

# 파이선함수
# def 함수이름(매개변수):

# 함수 실행 -> 함수이름()

""" 
def sum(a,b):
  return a+b
res = sum(10,20)
print(res)  

def func():
  print("나 함수다.")
func()  

def func1(word):
  print(word+"이다.")

func1("gd")

def minus(num1,num2):
  print(num1-num2)
minus(10,15)  

def whoam1(name,what):
  if name == "장영주":
    print(name+"는(은) " + what + "이다.")
  else:
    print(name + "는(은) " + what + "가 아니다")

whoam1("장영주","바보")
whoam1("김지연","바보")

cnt1 = 0
def count2():
  global cnt1
  cnt1+=1

while cnt1<10:
  count2()
print(cnt1)    
 """


# num1 = int(input("정수입력 : "))

# def num():
#   global num1
#   print(num1+100)

# num()  

""" 
def x(num1,num2):
  print(num1*num2)

num1 = int(input("정수1 : "))
num2 = int(input("정수2 : "))

x(num1,num2)
 """
""" 
def res(li):
  for i in li:
    print(i+1)

li = [i for i in range(0,51,2)]

res(li)
 """
""" 
def score_input(subj):
  scr = []
  for tmp in range(len(subj)):
    scr.append(int(input(subj[tmp])))
  return scr



def total(score):
  sum = 0
  for tmp in score:
    sum += tmp
  return sum 


def avg(sum):
  print(sum/3)
  
  
score = []
subj = ["국어점수","영어점수","물리치료"]

score = score_input(subj)  
sum = total(score)
avg(sum)
"""

#내가푼거
""" 
def score_ipt(name):
  score=[]
  for tmp in range(len(name)):
    score.append(int(input(name[tmp]+"의 키: ")))
  return score

name = ["장영순","김지언","이지형"]
temp = []

def avg(temp):
  sum = 0
  for tmp in temp:
    sum += tmp
  ag = int(sum /3)
  print("평균키 : {0}cm".format(ag)) 
  return ag

def min_avg(min):
  global temp
  global name
  m_num = []
  for i in range(len(temp)):
    if min > temp[i]:
      m_num.append(name[i])
  print("평균보다 작은사람 : {0}".format(",".join(m_num)))   

temp = score_ipt(name)
min = avg(temp) 
min_avg(min)
 """

#쌤정답
""" 
def smail(avg,tall):
  global cut
  for i in range(len(tall)):
    if avg > tall[i] :
      print("평균보다 작은사람 : {}".format(cut[i]))

def tall_avg(tall,소녀들):
  sum = 0
  for 소녀키 in tall:
    sum+=소녀키
  avg = int(sum/len(tall))
  print("평균키 : " + str(avg))
  smail(avg,tall)

def tall_ipt():
  global cut
  tall = []
  for 소녀 in cut:
    tall.append(int(input(소녀)))
  tall_avg(tall,cut)  

cut = ("장영순","이지형","김지언")
tall_ipt()
 """

""" 
li = list()
for i in range(1,51):
  li.append(i)

def five():
  global li
  for i in li:
    if i % 5 == 0:
      print(i)

five()      
 """

""" 
def func(a,b,c):
  print(a,b,c)

func("a","b","c")

def func1(na = "계림국"):
  print(na)
func1("대한민국")
func1()


def func2(**info):
  print(info["name"])
func2(name="장영주")  
 """
#,

li = ("이순신","장영실","정몽주","이성계","이방지")
li1 = list()
li2 = list()

for i in range(len(li)):
  li1.append(int(input(li[i]+"키 : ")))
  li2.append(int(input(li[i]+"몸무게 : ")))

def max_m(li2):
  global li
  max_mom=0
  max_name = ""
  for i in range(len(li)):
    if max_mom < li2[i]:
      max_mom = li2[i]
      max_name = li[i]
  print("몸무게가 큰사람 : {0} , 몸무게 : {1}".format(max_name,max_mom))

def min_k(li1):
  global li
  min_ki = li1[0]
  min_name = li[0]
  for i in range(len(li)):
    if li1[i] < min_ki:
      min_ki = li1[i]
      min_name = li[i]
      
  print("키가 작은사람 : {0} , 키 : {1}".format(min_name,min_ki))   


max_m(li2)

min_k(li1)


