
keys = ["번호","이름","연락처","이메일","성별","도시"]

# 딕셔너리 저장함수
def push(files):  
  global keys
  for i in range(len(files)):
    files[i] = files[i][:len(files[i])-1]
    files[i] = files[i].split(" ") 
  qus = dict()
  for i in range(len(files)):
    qus[i+1] = dict(zip(keys,files[i]))  
  return qus

# 파일로드함수
def ipt():
  file = []
  with open("c:/test/member.txt","r",encoding="utf-8") as f:
    file = f.readlines()
  return file

files = ipt()
a = push(files)

# 이메일 분리함수
def email_res(a):
  email= []
  # global domain
  email_temp = []
  for tmp in a:
    email = a[tmp]["이메일"].split("@") 
    email_temp.append(email[1]) 
  return email_temp

# naver 사용하는 도시
def dosi(a):
  email= []
  for tmp in a:
    email = a[tmp]["이메일"].split("@")
    if "naver.com" in email[1]:
      print("naver.com 도메인을 사용하는 사람의 도시 : "+a[tmp][keys[5]])
dosi(a)  

# 도메인 개수 함수 
def dom(e_ipt):
  cnt = [0,0,0]
  email_tmp = set(e_ipt)
  for tmp in a:
    email_list = list(email_tmp)
    if email_list[0] in a[tmp]["이메일"]:
      cnt[0]+=1
    elif email_list[1] in a[tmp]["이메일"]:
      cnt[1]+=1
    else:
      cnt[2]+=1    
  print("도메인 총 개수 : {3} naver 개수 : {0} daum 개수 : {1} google 개수 : {2}".format(cnt[0],cnt[1],cnt[2],len(email_tmp)))  
e_ipt = email_res(a)  
dom(e_ipt)

# 여자이면서 중구에서 사는 사람 함수

def woman(a,성별 ="여"):
  # global domain
  for tmp in a:
    if 성별 in a[tmp]["성별"] and "중구" in a[tmp]["도시"].split("-")[1]:
        print(a[tmp])
성별 = input("성별입력 : ")
woman(a,성별)      
