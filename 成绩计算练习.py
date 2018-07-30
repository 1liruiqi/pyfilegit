num = int(input("请输入成绩："))

if 90 <= num <= 100:
    print("等级是A")
elif 80 <= num < 90:
    print("等级是B")
elif 70 <= num < 80:
    print("等级是C")
elif 60 <= num < 70:
    print("等级是D")
elif 0 <= num < 60:
    print("不及格")
else:
    print("输入数字不规范！")