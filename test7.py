city = ("서울","대전","대구","광주","부산","울산","세종")
import random
# 각 도시의 신생아, 초등학생, 중학생, 고등학생, 대학생, 노년층의 인구수를 입력하시오.
# 딕셔너리 저장
# 어떤것이 키이고 어떤것이 value를 들어갈지 생각
age = ("신생아","초등학생","중학생","고등학생","대학생","노년층")
info = dict()
# for tmp in city:
#   data = []
#   for j in age:
#     data.append(input(j + ": "))
#   info.append(data)  

# dic = dict()
# for i in range(len(city)):
#   dic[city[i]] = dict(zip(age,info[i]))

# for i in dic:
#   print("{0} : {1}".format(i,dic[i]))

for cname in city:
  temp = dict()
  print("==== {0}의 인구수 ====".format(cname))
  for k in age:
    i = random.randint(1000,30000)
    print("{0} : {1}명".format(k,i))
    temp[k] = i
  info[cname] = temp
for i in info:
 
  print("{0} : {1}".format(i,info[i])) 