import random
import math

""" 
name = ["김유신","이순신","어영담","이성계","장영실","홍길동","김지연","김춘추"]
job = ["군인","국회의원","과학자","도적","건설업자","벨리댄서","변호사"]
age = [24,35,37,21,54,41,29,35,42]

info=[]

for i in range(10):
  info.append([random.choice(name),random.choice(job),random.choice(age)])

age_sum = 0  
age_avg = 0
names = []
jobs = []
name_result = ""
for tmp in info:
  if "군인" in tmp:
    names.append(tmp[0])

  if "과학자" in tmp:
    age_sum+=tmp[2]
    age_avg = age_sum/len(tmp)

  if tmp[2] >= 20 and tmp[2] < 30:
    jobs.append(tmp[1])

age_avg = math.ceil(age_avg)

# name_result = list(set(names))
# job_result = list(set(jobs))

print(" ".join(names))
print(str(age_avg)+"세")     
print(" ".join(jobs))
 """
""" 
a = []
b = []
c = []

num = []

for i in range(1,16):
  a.append(random.randint(1,30))

for i in range(1,16):
  b.append(random.randint(10,50))

for i in range(1,16):
  c.append(random.randint(1,100))    

print(a)
print(b)
print(c)

for tmp1 in a:
  for tmp2 in b:
    for tmp3 in c:
      if tmp1 == tmp2 == tmp3:
        num.append(tmp1)

if len(num) != 0:
  print("중복값은 : " + str(list(set(num))))        
else :
  print("없다") 


# 쌤정답
  for x in a:
    if x in b:
      if x in c:
        num.append(x)
 """

word = ["boy","table","book","girl","interest","limit","endless","mission","hopi","tigerprint"]

eng = ["a","b","c","d","e","f","g","h","j","k","l","m","n","o","p","q","r","s","t","u","v","w","y","z"]

s = ""
count = 0

while True:
  count+=1
  l = random.randint(3,10)
  for i in range(l):
    s += random.choice(eng)
  if s in word:
    break
  s=""

print(s+" 횟수 : " + str(count))