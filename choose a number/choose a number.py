import random
import string
print("easy:1-2,middle:2,3,hard:4")
number=string.digits
file=list(number)
a=random.shuffle(file)
long=int(input("please select the number long"))
b="".join(file[:long])
print("=============game start===============")
while True:
  choose=input("please write a number")
  if choose==b:
    print("you are correct")
    break
  elif choose>b:
    print("smaller")
  elif choose<b:
    print("bigger")  