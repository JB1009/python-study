""" 
dic = {"이름":"이순신","나이":24,"직업":"군인"}

print(dic)
print(dic["이름"])

dic = {}
dic = dict()

dic1 = dict(이름="김지연",나이=29,직업="마이쮸판매")

print(dic1["이름"])

dic2 = dict([("이름","이지현"),("age",26),("특징","알면서")])
print(dic2)

dic3 = dict(zip(["이름","나이","관심분야"],["윤재영",25,"컴퓨터선생님"]))
print(dic3)

dic3["관심분야"] = "지연이누나"
print(dic3)

dic3["싫어하는것"] = "옆반선생님"
print(dic3)

if "이름" in dic3:
  print("너의이름은 {0}".format(dic3["이름"]))
else:
  print("존재하지않는 키입니다.") 


title = ["캐릭터명","생명력","코딩기술","잔머리","수학능력","공간능력","지능지수"]

data = []
for x in title:
  data.append(input(x + ": "))



info = dict(zip(title,data))
print(info)

for tmp in info:
  print(info[tmp])

for tmp in info.values():
  print(tmp)

for tmp in info.keys():
  print(tmp)  

for k,v in info.items():
  print(k,v)  
 """
""" 
title = ["이름","키","몸무게","관심분야"]
info = []
while len(info) < 5:
  data=[]
  for tmp in title:
    data.append(input(tmp+": "))
  info.append(data)  



dic_info  = dict()

for data in info:
  dic_info[data[0]] = data
print(dic_info)  

 """
""" 
keys = ["이름","번호","c언어성적","java성적","react성적","DB성적","지적수준"]

values = list()
while len(values) < 3:
  temp = list()
  for tmp in keys:
    temp.append(input(tmp+": "))
  values.append(temp)
avg = 0
class501 = dict()


for v in values:
  class501[v[0]] = dict(zip(keys,v))


for k in class501:
  print("{0} : {1}".format(k,class501[k]))

avg = list()
dic_avg = dict()
for name in class501:
  sum = 0
  #1번
  title = list(class501[name].keys())
  for i in range(2,6):
    sum += int(class501[name][title[i]])

  #2번
  # score = list(class501[name].values()) 
  # for i in range(2,6):
  #   sum += int(score[i]) 

  # 3번
  # for title in class501[name]:
  #   if title == "이름" or title == "번호" or title == "지적수준":
  #     continue
  #   else:
  #     sum += int(class501[name][title])
  dic_avg[name] = dict(평균점수 = sum/4,지적수준 = class501[name]["지적수준"])
        
print(dic_avg)

 """
f = open("c:/test/question.txt","r",encoding="utf-8")

line = f.readlines()

f.close()
file = []
with open("c:/test/question.txt","r",encoding="utf-8") as f:
  file = f.readlines()

keys = ["문의제목","작성자","문의내용","작성일","답변","답변일"]  
dic = dict()

for i in range(len(file)):
  file[i] = file[i][:len(file[i])-1]
  file[i] = file[i].split(" ")

# for i in range(1,len(file)+1):
#   dic[i] = dict(zip(keys,file[i-1]))

# for k in dic:
#   print("{0}: {1}".format(k,dic[k]))

qus = dict()
for i in range(len(file)):
  qus[i+1] = dict(zip(keys,file[i]))

# print(qus)  



ti = ["문의제목","작성일"]
for tmp in qus:
  print(tmp,qus[tmp][ti[0]],qus[tmp][ti[1]])  
num = int(input("번호입력 : "))
print()


print("작성자 : " + qus[num][keys[1]])
print("제목 : " + qus[num][keys[0]])
print("작성일 : " + qus[num][keys[3]])
print("문의글 : " + qus[num][keys[2]])
print("==========================")
print("답변 : " + qus[num][keys[4]])
print("답변일 : " + qus[num][keys[5]]+"\n")
