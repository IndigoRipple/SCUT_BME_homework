import English_names as E
import random
import time
import os

random.seed(time.time())

class Teacher():
    def __init__(self,name,course_name):
        self.name=name
        self.course_name=course_name
            
class Course():
    def __init__(self,name,score,teacher_name):
        self.name=name
        self.score=score
        self.Teacher=Teacher(teacher_name,name)

class Student():
    def __init__(self,Name,Class,math,english,python):
        self.name=Name
        self.Class=Class
        self.Courses=[]
        self.Courses.append(Course("Math",math,"John"))#random.randint(0,100)
        self.Courses.append(Course("English",english,"Peter"))
        self.Courses.append(Course("Python",python,"Brine"))
        self.sum_score=0
        for i in self.Courses:
            self.sum_score += i.score
    def __gt__(self,b):
        if self.sum_score>b.sum_score:
            return False
        return True

class Class():
    def __init__(self):
        self.Students=[]
    def add(self,x):
        self.Students.append(x)
    def size(self):
        cnt=0
        for i in self.Students:
            cnt+=1
        return cnt
    def sort(self):
        self.Students.sort()

A=Class()
B=Class()
math_teacher=Teacher("John","Math")
eng_teacher=Teacher("Peter","English")
py_teacher=Teacher("Brine","Python")


def query_student_score(a_student):#传入Student类型
    print("Class:"+a_student.Class)
    print("---------------------"+a_student.name+"'s scores:")
    sum=0
    for i in a_student.Courses:
        sum+=i.score
        print(i.name+"("+i.Teacher.name+")"+":"+str(i.score))
    print("sum:"+str(sum))

def query_teacher_score(a_teacher):#传入Teacher类型
    global A,B
    print(a_teacher.course_name+"'s scores is below")
    if(a_teacher.course_name=="Math"):
        print("Students in Class A:")
        if(A.size()==0):
            print("No Data")
        else:
            max_,min_,sum_=(0,100,0)
            for i in A.Students:
                print(i.name+":"+str(i.Courses[0].score))
                sum_+=int(i.Courses[0].score)
                max_=max(max_,i.Courses[0].score)
                min_=min(min_,i.Courses[0].score)
            print("--------------------")
            print("AVG:%f"%(sum_/A.size()))
            print("MAX:%d"%max_)
            print("MIN:%d"%min_)
            print()
        print("Students in Class B:")
        if(B.size()==0):
            print("No Data")
        else:
            max_,min_,sum_=(0,100,0)
            for i in B.Students:
                print(i.name+":"+str(i.Courses[0].score))
                sum_+=i.Courses[0].score
                max_=max(max_,i.Courses[0].score)
                min_=min(min_,i.Courses[0].score)
            print("--------------------")
            print("AVG:%f"%(sum_/B.size()))
            print("MAX:%d"%max_)
            print("MIN:%d"%min_)
    if(a_teacher.course_name=="English"):
        print("Students in Class A:")
        if(A.size()==0):
            print("No Data")
        else:
            max_,min_,sum_=(0,100,0)
            for i in A.Students:
                print(i.name+":"+str(i.Courses[1].score))
                sum_+=int(i.Courses[1].score)
                max_=max(max_,i.Courses[1].score)
                min_=min(min_,i.Courses[1].score)
            print("--------------------")
            print("AVG:%f"%(sum_/A.size()))
            print("MAX:%d"%max_)
            print("MIN:%d"%min_)
            print()
        print("Students in Class B:")
        if(B.size()==0):
            print("No Data")
        else:
            max_,min_,sum_=(0,100,0)
            for i in B.Students:
                print(i.name+":"+str(i.Courses[1].score))
                sum_+=i.Courses[1].score
                max_=max(max_,i.Courses[1].score)
                min_=min(min_,i.Courses[1].score)
            print("--------------------")
            print("AVG:%f"%(sum_/B.size()))
            print("MAX:%d"%max_)
            print("MIN:%d"%min_)
    if(a_teacher.course_name=="Python"):
        print("Students in Class A:")
        if(A.size()==0):
            print("No Data")
        else:
            max_,min_,sum_=(0,100,0)
            for i in A.Students:
                print(i.name+":"+str(i.Courses[2].score))
                sum_+=int(i.Courses[2].score)
                max_=max(max_,i.Courses[2].score)
                min_=min(min_,i.Courses[2].score)
            print("--------------------")
            print("AVG:%f"%(sum_/A.size()))
            print("MAX:%d"%max_)
            print("MIN:%d"%min_)
            print()
        print("Students in Class B:")
        if(B.size()==0):
            print("No Data")
        else:
            max_,min_,sum_=(0,100,0)
            for i in B.Students:
                print(i.name+":"+str(i.Courses[2].score))
                sum_+=i.Courses[2].score
                max_=max(max_,i.Courses[2].score)
                min_=min(min_,i.Courses[2].score)
            print("--------------------")
            print("AVG:%f"%(sum_/B.size()))
            print("MAX:%d"%max_)
            print("MIN:%d"%min_)

print("Welcome to Project2 !")

print("输入'/add'以添加学生信息")
print("输入'/init'快速初始化至满班")
print("输入'/query'以查询学生成绩单")
print("输入'/display'以查询单科成绩单")
print("输入'/rank'以查询班级排名")
print("输入'/cls'以清屏")
print("输入'/exit'以退出")
print("—————————————————————————————————")
while (True):
    print("输入'/help'以获取命令集")
    s=input("请输入命令:")
    if(s=="/add"):
        opt=False
        Name= input("Name  :")
        Class=input("Class :")
        Score_math=int(input("Math Score:"))
        Score_english=int(input("English Score:"))
        Score_python=int(input("Python Score:"))
        new_student=Student(Name,Class,Score_math,Score_english,Score_python)
        if(Class=="A"):
            A.add(new_student)
            opt=True
        if(Class=="B"):
            B.add(new_student)
            opt=True
        if(opt==True):
            print("添加成功！\n")
        if(opt==False):
            print("添加失败！\n")
    elif(s=="/init"):
        while(A.size()<20 or B.size()<20):
            Name= E.get_name()
            Score_math=random.randint(0,100)
            Score_english=random.randint(0,100)
            Score_python=random.randint(0,100)
            if A.size()<20:
                Class="A"
                new_student=Student(Name,Class,Score_math,Score_english,Score_python)
                A.add(new_student)
            else :
                Class="B"
                new_student=Student(Name,Class,Score_math,Score_english,Score_python)
                B.add(new_student)
        print("初始化成功！\n")
    elif(s=="/query"):
        opt=False
        Name=input("Student's name:   ")
        for i in A.Students:
            if(i.name==Name):
                opt=True
                query_student_score(i)
                break
        for i in B.Students:
            if(i.name==Name):
                opt=True
                query_student_score(i)
                break
        if(opt==False):
            print("查询失败!")

    elif(s=="/display"):
        print(math_teacher.name+"(Math)  "+eng_teacher.name+"(English)  "+py_teacher.name+"(Python)")
        Name=input("Teacher's name:   ")
        if(Name==math_teacher.name):
            query_teacher_score(math_teacher)
        elif(Name==eng_teacher.name):
            query_teacher_score(eng_teacher)
        elif(Name==py_teacher.name):
            query_teacher_score(py_teacher)
        else:
            print("查询失败!")
    elif(s=="/rank"):
        A.sort()
        B.sort()
        print("-----------Class A:")
        for i in A.Students:
            print(i.name+":"+str(i.sum_score))
        print("-----------Class B:")
        for i in B.Students:
            print(i.name+":"+str(i.sum_score))
    elif(s=="/help"):
        print("—————————————————————————————————")
        print("Welcome to Project2 !")
        print("输入'/add'以添加学生信息")
        print("输入'/init'快速初始化至满班")
        print("输入'/query'以查询学生成绩单")
        print("输入'/display'以查看单科成绩单")
        print("输入'/rank'以查看班级排名")
        print("输入'/cls'以清屏")
        print("输入'/exit'以退出")
    elif(s=="/cls"):
        os.system('cls')
    elif(s=="/exit"):
        print("已退出")
        break
    else:
        print("输入无效！\n")
    A.sort()
    B.sort()
    
