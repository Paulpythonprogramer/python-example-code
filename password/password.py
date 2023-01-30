import random
import string
number=string.digits
english=string.ascii_letters
file=list(number+english)
random.shuffle(file)
long=int(input("你要幾位數的密碼:"))
password="".join(file[:long])
print(f"{password}")
  