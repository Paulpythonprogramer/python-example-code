def 加法(x,y):
    return x+y
def 減法(x,y):
    return x-y    
def 乘法(x,y):
    return x*y
def 除法(x,y):
    return x/y
while True:
    計算類型=input("請輸入要操作的指令(1)加(2)減(3)乘(4)除:")
    if 計算類型 in ("1","2","3","4"):
     no1=int(input("請輸入第一個數字:"))
     no2=int(input("請輸入第二個數字:"))
     if 計算類型=="1":
        print(f"{no1}+{no2}={加法(no1,no2)}")
     elif 計算類型=="2":
         print(f"{no1}-{no2}={減法(no1,no2)}")
     elif 計算類型=="3":
        print(f"{no1}*{no2}={乘法(no1,no2)}")
     elif 計算類型=="4":
        print(f"{no1}/{no2}={除法(no1,no2)}")        
    else:
        print("error")
        break