import pandas as pd
import os


class SMS(object):
    def __init__(self, id, name, age, sex, clas):
        self.ID = str(id)
        self.name = str(name)
        self.age = str(age)
        self.sex = str(sex)
        self.clas = str(clas)
    def change_id(self, id):
        self.ID = id
    def change_name(self, name):
        self.name = name
    def change_age(self, age):
        self.age = age
    def change_sex(self, sex):
        self.sex = sex
    def change_clas(self, clas):
        self.clas = clas
    def __str__(self):
        return str(self.ID)+" "+str(self.name)+" "+str(self.age)+" "+str(self.sex)+" "+str(self.clas)
def get_id(s):
    return s.ID
def get_name(s):
    return s.name
def get_age(s):
    return s.age
def get_sex(s):
    return s.sex
def get_clas(s):
    return s.clas


students=[]
f=pd.read_excel("姓名.xlsx")
for i in range(31):
    m=SMS(f.iloc[i][1],f.iloc[i][0],f.iloc[i][3],f.iloc[i][2],"BME2")
    students.append(m)



print("Welcome to Student Management System in BME!")
print("输入'/help'以获取命令集")
print("输入'/add'以添加")
print("输入'/delete'以删除")
print("输入'/updata'以更新")
print("输入'/query'以查询")
print("输入'/display'以查看全部数据")
print("输入'/cls'以清屏")
print("输入'/exit'以退出")
print("—————————————————————————————————")
while (True):
    print("输入'/help'以获取命令集")
    s=input("请输入命令:")
    if(s=="/add"):
        ID  =input("ID:   ")
        name=input("Name: ")
        age =int(input("Age:  "))
        sex =input("Sex:  ")
        clas=input("Class:")
        if(age>=100):     #待商榷
            print("操作失败!\n")
        elif(sex!='男' and sex!='女'):
            print("操作失败!\n")
        else:
            new_student=SMS(ID,name,age,sex,clas)
            students.append(new_student)
            print("操作成功!\n")
    elif(s=="/delete"):
        opt=False
        ID  =input("ID:   ")
        for i in students:
            if(get_id(i)==ID):
                opt=True
                students.remove(i)
                print("操作成功!\n")
        if(not opt):
            print("操作失败!\n")
    elif(s=="/updata"):
        opt=False
        ID  =input("ID:   ")
        for i in students:
            if(get_id(i)==ID):
                opt=True
                print("Name :",get_name(i))
                print("Age  :",get_age(i))
                print("Sex  :",get_sex(i))
                print("Class:",get_clas(i))
                print("—————————————————————————————————\n你想修改哪一项(输入括号内的字母并回车)?")
                print("Name(N) Age(A) Sex(S) Class(C)")
                change_=input("input your choise:")
                if(change_=='N'):
                    change_char=input("%s'name change to:"%ID)
                    i.change_name(change_char)        
                    print("操作成功!\n")
                    break
                elif(change_=='A'):
                    change_char=input("%s'age change to:"%ID)
                    i.change_age(change_char)
                    print("操作成功!\n")
                    break
                elif(change_=='S'):
                    change_char=input("%s'sex change to:"%ID)
                    i.change_sex(change_char)
                    print("操作成功!\n")
                    break
                elif(change_=='C'):
                    change_char=input("%s'class change to:"%ID)
                    i.change_clas(change_char)
                    print("操作成功!\n")
                    break
                else:
                    print("操作失败!\n")
                    break
        if(not opt):
            print("操作失败!\n")
    elif(s=="/query"):
        ID  =input("ID:   ")
        for i in students:
            if(get_id(i)==ID):
                print("Name :",get_name(i))
                print("Age  :",get_age(i))
                print("Sex  :",get_sex(i))
                print("Class:",get_clas(i))
                print()
                break
    elif(s=="/display"):
        for i in students:
            print(i)
        print()
    elif(s=="/help"):
        print("—————————————————————————————————")
        print("Welcome to Student Management System in BME!")
        print("输入'/add'以添加")
        print("输入'/delete'以删除")
        print("输入'/updata'以更新")
        print("输入'/query'以查询")
        print("输入'/cls'以清屏")
        print("输入'/display'以查看全部数据")
        print("输入'/exit'以退出")
    elif(s=="/cls"):
        os.system('cls')
    elif(s=="/exit"):
        print("已退出SYS并保存数据于'a.txt'！")
        break
    else:
        print("无效输入!\n")
    op=open("a.txt",'w')
    for i in students:
        op.write(str(i.ID)+" "+str(i.name)+" "+str(i.age)+" "+str(i.sex)+" "+str(i.clas)+'\n')
    op.close()

