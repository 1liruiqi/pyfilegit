active = True
while active:
    mile = int(input("请输入公里数："))
    if 0 < mile < 2:
        print("所需费用为：8元")
    elif 2 < mile < 12:
        pay = 8 + (mile-2)*1.2
        print("所需费用为：",pay)
    elif 12 < mile:
        pay = 8 + (mile-2)*1.5
        print("所需费用为：",pay)
    else:
        print("请输入正确的公里数进行计算")
        active = False