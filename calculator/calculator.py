def plus(x,y):
    return x+y
def minus(x,y):
    return x-y    
def multiplication(x,y):
    return x*y
def division(x,y):
    return x/y
while True:
    calculation_type=input("please select the service(1)plus(2)minus(3)multiplication(4)division:")
    if calculation_type in ("1","2","3","4"):
     no1=int(input("Please enter the first number:"))
     no2=int(input("Please enter the second number:"))
     if calculation_type=="1":
        print(f"{no1}+{no2}={plus(no1,no2)}")
     elif calculation_type=="2":
         print(f"{no1}-{no2}={minus(no1,no2)}")
     elif calculation_type=="3":
        print(f"{no1}*{no2}={multiplication(no1,no2)}")
     elif calculation_type=="4":
        print(f"{no1}/{no2}={division(no1,no2)}")
        if calculation_type==1/0:
            print("ZeroDivisionError: division by zero")                  
    else:
        print("error")
        break