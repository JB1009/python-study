import random

""" print("asd")
1번
v = float(input("속력"))
r = float(input("반지름"))

dist = r*2*3.14

time = dist/v*60

print("완주시간 {0:.1f}분".format(time))




soju = int(input("소주잔"))

life = soju * 2 * 365 * 20

print("단축수명 : {0}".format(life))
print("단축수명 : {0}".format(int(life/60)))
print("단축수명 : {0}".format(int(life/60/24)))



x,y,z = "김지연","장영주","변수정"

favorite = ["목발","선인장","19남친"]  

a,b,c = favorite
print(a)
print(b)
print(c)

num = 19
num1 = 27

if num1 > num : 
  print("누난 내 여자니까!")
else:
  print("누나 늙었어")
  print("이건 그냥 출력")

age = 22

if age > num : 
  print("ㅎㅇ")
elif num > age :
  print("ㅂㅇ")
else : 
  print("둘다 ㅂㅇ")

name = "김지연"

print("미안합니다.. 그만할게요") if name == "김지연" else print("농일세") if num1 != 27 else print("뻥인데 계속할건데")


지연 = int(input("지연점수 : "))
기원 = int(input("기원점수 : "))

if 지연 > 기원 :
  print("지연 승")
elif 지연 == 기원 :
  지연 = random.randrange(1, 1001)
  기원 = random.randrange(1, 1001)
  if 지연 > 기원 :
    print("지연 승 " + str(지연) + "점")
  elif 기원 > 지연 : 
    print("기원 승 " + str(기원) + "점")
  else : 
    print("무승부")
else : 
  print("기원 승")


영주 = random.randrange(1, 101)
지연 = random.randrange(1, 101)
수정 = random.randrange(1, 101)

avg = (영주 + 지연 + 수정) / 3
print("영주 점수 : " + str(영주) + "점" + " 지연 점수 : " + str(지연)+ "점"  + " 수정 점수 : " + str(수정)+ "점" )
if avg > 90 :
  print("A")
elif avg > 80 : 
  print("B")  
elif avg > 70 :
  print("C")
else : 
  print("쯧쯧...") 


i = 4
k = 1
while k <= 9:
  print(str(i) + " * " + str(k) + " = " + str(i*k))
  k += 1



i =1

while i<5:
  print(i)
  i+=1
else : 
  print("5보다 크면 반복문 종료")

i=1
while True:
  print(i)
  if i==100: break
  i+=1

BUS_PAY = 1200
money =  10000
count = 0

while money >= BUS_PAY :
  money -= BUS_PAY
  count += 1
  
print("탑승 횟수 : " + str(count) + "회 남은잔액 : " + str(money) + "원")

num = 8
for i in range(2,10):
  for j in range(1,10):
    print(str(i) + " * " + str(j) + " = " + str(j*i))
print("")

for i in range(1,10):
  print("{0} * {1} = {2}".format(num,i,num*i))


for i in range(45,110):
  print(i)

for i in range(1,101):
  if i % 3 == 0 :
    print("윤재영",end="")
  if i % 5 == 0 :
    print("바보")
  else :
    print(i)

  파이선 데이터 타입
  리스트 , 튜플 , 딕셔너리 , 셋 , 배열

 
name = [ "장영주바보","김지연똥개","윤재영멍충이" ]
print(name)
data1 = ["김기원장",100,3.14,True]
print(data1)

data2 = list(("최윤도서관","변수정과",100))
print(data2)

print(data2[0])
print(data2[-1])

data3 = ["이종빈티지","윤종찬양하라","이지현미밥맛있어","장영주모"]
print(data3[1:3])
print(data3[:3])
print(data3[2:])

data3.append("김지연기하네")
data3.append("윤재영영사랑해")
print(data3)

data3.remove("장영주모")
print(data3)
data3.pop()
print(data3)
del data3[2]
print(data3)

data3.clear()
print(data3)
 """
""" 
memo = [ " 나"," 김지연","은"," 19세 남친을"," 원한다" ]
for i in memo:
  print(i,end="")

memo[3] = " 대머리 남친들"
print("")
for me in memo:
  print(me,end="")

memo[1:4] = [" 장영주","는"," 목발을"]
print()
for st in memo:
  print(st,end="")
print()
memo.insert(3," 드러운 어그와 ")
print(memo)

memo1 = ["이종빈","윤재영","변수정"]
memo2 = ["장영주부","김지연세많음","이지현왕언니"]
memo1.extend(memo2)
print(memo1)
print(len(memo1))


 리스트 생성
 1. memo = ["a","b","c"]
 2. memo = list(("장","영","주","땡"))
  데이터 추가 memo.append("리정수")
  데이터 삽입 memo.insert(2,"김민정수리")
  데이터 삭제
  삭제 데이터 지정 memo.remove("떙")
  마지막데이터삭제 memo.pop()
  인덱스로 삭제 del memo[3]
  리스트 합치기 memo.extend(리스트)
  리스트 크기 len(리스트) 
  갯수구하기 memo.count("장") - 장이라는 데이터가 몇개인가
  인덱스찾기 memo.index("영") - 영이라는 데이터가 몇번인덱스에있나
  정렬 memo.sort() , memo.sort(reverse=True) 
  반전 memo.reverse() 
  """
# info501 = ["장영주는 폭력적이다.","김지연은 연하만 좋아한다","윤재영은 옆반쌤을 좋아한다","최윤도는 영주불행이 행복이다","수정이는 생일이라 코딩이 싫대.. ","종빈이는 지금 게임한다 "]

# name = input("딸기반 학생 이름 : ")
# for i in info501:
#   infoName = i[:3]
#   if name == infoName:
#     print(i)
  
# for na in info501:
#   if name in na:
#     print(na)
  
# for i in info501:
#   if "좋아한다" in i:
#     print(i)
num = [x for x in range(10)]
print(num)