a = int(input("Введите год: "))
if a%4 == 0 or a%400 == 0:
    if a%100 != 0:
        print("Год", a ,"- високосный")
else:
    print("Год", a ,"- не високосный")