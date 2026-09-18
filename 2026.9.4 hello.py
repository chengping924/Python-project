while True:
    name = input("請輸入你的名字：")
    if name=="":
        print("名字輸入錯誤，請重新輸入!\n")
    else:
        break
print("Hello, " + name +"!")
#下面為強迫桌面視窗停住
input("\n按下 Enter 鍵結束應用程式")