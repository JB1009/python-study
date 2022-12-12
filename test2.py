import random
# num = random.randint(1,3)
# print(num)  


# firstName = ["김","장","이","최","윤","변"]
# middle = ["기","지","영","윤","재","종","수","민","다"]
# last = ["원","연","현","영","도","똥","순","숙"]

# ran1 = random.choice(firstName)
# ran2 = random.choice(middle)
# ran3 = random.choice(last)
# print(ran1,ran2,ran3)


# info = [["김기원","콘샐러드","시험"],["이지현","나이","민감"],["김지연","배꼽","선생님배꼽찔러봄"],["장영주","후크","공통점"],["윤재영","비니","강균성"],["리정수","군대","인민군"]]

# for i in info:
#   for j in i:
#     print(j)

# st = input("입력 : ")

# for i in info:
#   for j in i:
#     if st in i:
#       print(j)
#       break
      
info = [["김민서","군인",28],["정다현","디자이너",45],["장영주","트럭기사",61],["김지연","밸리댄서",34],["윤재영","수필가",58],["최윤도","모필가",24],["변수정","멕시코음식전문점사장",33],["이종빈","프로게이머연습상대",39],["윤종찬","파이터only서린",22],["이지현","뒷방...",69],["이정수","초딩",11],["김민정","헤어디자이너샘플",28]]
age30 = []
num = 0 
age = [0,0,0,0,0,0,0]
연장자 = ""
for num_list in info:
  age[int(num_list[2]/10)] += 1
  if num_list[2] > 29 and num_list[2] < 40:
    age30.append(num_list[1])
  if num < num_list[2]:
    num = num_list[2]
    연장자 = num_list
    # if num < num_list[2]:
    # print(num_list)
print(age)
print(age30)
print(연장자)


