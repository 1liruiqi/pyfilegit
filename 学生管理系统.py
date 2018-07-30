students = []

def add_students():
    name = input("请输入名字：")
    age = input("请输入年龄：")
    number = input("请输入学号：")
    student = {'name':name,'age':age,'id':number}
    students.append(student)

def change_students():
    if students != []:
        id = int(input("请输入要改变的学生序号："))
        name = input("请输入该学生新的名字：")
        age = input("请输入该学生新的年龄：")
        number = input("请输入该学生新的学号：")
        student = {'name': name, 'age': age, 'id': number}
        students[id - 1] = student
        print("您已成功修改了该学生信息！")
    else:
        print("暂无学生信息！")
def find_students():
    if students != []:
        id = int(input("请输入要查询方式（1、通过序号查询单个学生；2、查询全部学生信息）："))
        if id == 1:
            query_num = int(input("请输入要查询的序号："))
            print(students[query_num - 1])
        elif id == 2:
            for student in students:
                print(student)
        else:
            print("输入格式不正确！")
    else:
        print("暂无学生信息！")

def rm_students():
    if students != []:
        id = int(input("请输入要删除的方式（1、通过序号删除单个学生；2、删除全部学生）："))
        if id == 1:
            del_num = int(input("请输入要删除的序号："))
            del students[del_num - 1]
            print("删除成功！")
        elif id == 2:
            del students[:]
            print("删除成功！")
        else:
            print("输入格式不正确!")
    else:
        print("暂无学生信息！")
def main():
    print("欢迎来到学生管理系统")
    print("----------menu----------")
    print("1、添加学生信息")
    print("2、修改学生信息")
    print("3、查找学生信息")
    print("4、删除学生信息")
    print("--------------------------")
    while True:
        key = input("请输入序号进行操作，按q退出！：")
        if key == '1':
            add_students()
        elif key == '2':
            change_students()
        elif key == '3':
            find_students()
        elif key == '4':
            rm_students()
        elif key == 'q':
            break
        else:
            print("输入格式有误！")
main()
