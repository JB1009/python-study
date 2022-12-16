# import random

# # f = open("c:/test/question.txt","r",encoding="utf-8")

# # line = f.readlines()
# # print(line)

# # f.close()
# file = []
# with open("c:/test/question.txt","r",encoding="utf-8") as f:
#   file = f.readlines()

# for i in range(len(file)):
#   file[i] = file[i][:len(file[i])-1]
#   file[i] = file[i].split(" ")

# slt = input("이름 또는 제품명 : ")
# print()

# # for tmp in file:
# #   if slt in tmp[1] or slt in tmp[0]:
# #     print("작성자 : " + tmp[1])
# #     print("제목 : " + tmp[0])
# #     print("작성일 : " + tmp[3])
# #     print("문의글 : " + tmp[2])
# #     print("==========================")
# #     print("답변 : " + tmp[4])
# #     print("답변일 : " + tmp[5]+"\n")

# # for tmp in file:
# #   for temp in tmp:
# #     if slt in temp:
# #       print("작성자 : " + tmp[1])
# #       print("제목 : " + tmp[0])
# #       print("작성일 : " + tmp[3])
# #       print("문의글 : " + tmp[2])
# #       print("==========================")
# #       print("답변 : " + tmp[4])
# #       print("답변일 : " + tmp[5]+"\n")
# #       break

# for tmp in file:
#   for i in range(len(tmp)):
#     if slt in tmp[i]:
#       print("작성자 : " + tmp[1])
#       print("제목 : " + tmp[0])
#       print("작성일 : " + tmp[3])
#       print("문의글 : " + tmp[2])
#       print("==========================")
#       print("답변 : " + tmp[4])
#       print("답변일 : " + tmp[5]+"\n")
#       break


""""
튜플
- 리스트처럼 데이터를 저장해두는 구조이다.
- 리스트처럼 여러데이터를 복합적으로 저장 가능하다.
- 하지만 튜플은 리스트와 다르게 변경이 안된다.
- 데이터 변경이 안될뿐 리스트와 동일하다
- 리스트의 표현태그는 [ ]이고 튜플은 ( )이다   
- 튜플은 데이터의갯수가 고정적으로 제한되어있는 경우 또는 데이터가 변경되지않는 경우에 사용
"""
# 튜플 생성
tu = "새신발","밟혔다"
print(tu)
print(type(tu))

tu1 =("그래서","주먹으로쳤다")
print(tu1)
tu2=("아프다")
print(type(tu2))
tu3 = ("하녀복장",)
print(type(tu3))
tu4 = ("그리고","난","발목을차였다","혼신의주먹을날릴뻔")
a,b,c,d = tu4
print(a,b,c,d)

print(tu4[2])
print(tu4[1:])
print(tu4.count("난"))