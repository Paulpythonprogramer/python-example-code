correctpassword="123456"
for times in range(5):
    password=input("請輸入密碼:")
    if password==correctpassword:
        print("登入成功")
        break
    elif password !=correctpassword and times <4:
        print("密碼錯誤")
        print(f"你還有{4-times}次機會")
    else:
        print("你已輸入太多次，帳戶已遭到鎖定")
    