print("欢迎来到非诚勿扰！我是主持人孟非，下面请输入男生信息：")
man_age = int(input("请输入男生年龄："))
man_height = int(input("请输入男生身高："))
man_weight = int(input("请输入男生体重："))
man_income = int(input("请输入男生收入："))
print()
print("请输入女生信息：")
woman_age = int(input("请输入女生年龄："))
woman_height = int(input("请输入女生身高："))
woman_weight = int(input("请输入女生体重："))
woman_income = int(input("请输入女生收入："))

def man_active():
    if 20 <= man_age <= 28 and 160 <= man_height <= 175 and 40 <= man_weight <= 60 and 2000 <= man_income <= 5000:
        man_active = True
        return man_active

def woman_active():
    if 20 <= woman_age <= 28 and 150 <= woman_height <= 170 and 40 <= woman_weight <= 55 and 2000 <= woman_income <= 4000:
        woman_active = True
        return woman_active

if man_active() and woman_active() == True:
    print("恭喜，配对成功！")
else:
    print("很遗憾，配对失败！")

