# set 
# 리스트와 달리 순서없이 중복없이 사용 
# 순서가 없다라는 말은 입력한 순서대로 저장되어있지않다. 
# 중복제거가 필요한경우에 사용 
# 그룹구성할때 사용(집합)
import random

""" set1 = {"사과","배","참외","배"," 배"}
print(set1)

set2 = {"member"}
print(set2)

set3 = set("장영죽이가 죽을 먹었다. 근데 장영죽이가 죽을 먹다 체했다.")
print(set3)
set4= set(("장영실이","수도원옷을","입었다"))
for s in set4:
  print(s)


print("장영주가" in set4)

set4.add("김진연은")

set5 = {"안경을 쓰고있다.","그래서","겨울에는 장님이된다."}
set4.update(set5)
print(set4)

list1 = ["장영주는","화가많다."]
set4.update(list1)
print(set4)

장영주팀 = {"김기원","김민서","김민정","최윤도","정다현","임성민","이지현","이종빈"}
김지연팀 = {"윤재영","이정수","윤종찬","변수정","최윤도","이지현","전계림","연하남친"}

a = 장영주팀 - 김지연팀 #차집합
print(a)
b = 장영주팀 | 김지연팀 #합집합
print(b)
c = 장영주팀 & 김지연팀 #교집합
print(c)
d = 김지연팀 ^ 장영주팀 #합집합에서 교집합
print(d)
a = 장영주팀.difference(김지연팀) #차집합
b = 장영주팀.intersection(김지연팀)#교집합
c = 장영주팀.symmetric_difference(김지연팀)#합집합

 """
""" 
이정수팀장 = {"김기원","최윤도","장영주","이종빈","정다현","김유신","한석봉","윤재영"}
이지현팀장 = {"김지연","윤재영","윤종찬","변수정","김유신","한석봉","이순신"}

스파이 = 이정수팀장.intersection(이지현팀장)

print("스파이 : {0}".format(스파이))

충신 = 이정수팀장 - 이지현팀장
print("이정수에게 충성맹세한자 : {0}".format(충신))

전계림추종자 = {"장영주","윤재영","김지연","이종빈"}

이바사 = 이지현팀장 - 이정수팀장
이바사 = 이바사 - 전계림추종자
print("완전한 이지현 사람들 : {0}".format(이바사))
 """

arr = set()
while len(arr) < 10:
  rand = random.randint(1,50)
  arr.add(rand)
  
print(arr)      


member = [["김춘추","01012345678","남"],["김지연","01054987924","여"],["이순신","01087954682","남"],["하지원","01078976545","여"],["전계림","01032220205","남"],["전지현","01054658797","여"],
          ["윤재순","01047858569","여"],["이지현","01088554488","여"],["이요원","01079794646","남"]]

print("======회원가입======")
name = input("이름 : ")

names = []
for x in member:
  names.append(x[0])
tempSet = set(names)
setName = {name}

while setName.issubset(tempSet):
  print("이름중복입니다. 다시입력하세요.")
  name = input("이름 : ")

tel = input("연락처 : ")
gender = input("성별 : ")

member.append([name,tel,gender])





# for i in range(len(member)):
#     if name in member[i][0] : 
#       print("있어 돌아가")
#       break
#     else:
#       member.append([name,tel,gender])
#       break

# print(member)



