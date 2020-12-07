import numpy as np 
from matplotlib import pyplot as plt 
import tkinter as tr
import tkinter.messagebox
import draw as dr
from PIL import Image, ImageTk

#绘画四种图像
def draw_age():
    plt.figure(figsize=(10,9))
    plt.title("Age table") 
    plt.xlabel("x axis caption") 
    plt.ylabel("y axis caption") 
    for i in range(16281):
        plt.plot(i,dr.datas[i].age,'.',) 
    #plt.legend(loc='best')
    plt.axis([0,16281,0,1])
    #plt.show()
    plt.savefig('age.jpg')

def draw_fnlwgt():
    plt.figure(figsize=(10,9))
    plt.title("Fnlwgt table") 
    plt.xlabel("x axis caption") 
    plt.ylabel("y axis caption") 
    for i in range(16281):
        plt.plot(i,dr.datas[i].fnlwgt,'.',) 
    #plt.legend(loc='best')
    plt.axis([0,16281,0,1])
    #plt.show()
    plt.savefig('fnlwgt.jpg')

def draw_education_num():
    plt.figure(figsize=(10,9))
    plt.title("Education-num table") 
    plt.xlabel("x axis caption") 
    plt.ylabel("y axis caption") 
    for i in range(16281):
        plt.plot(i,dr.datas[i].education_num,'.',) 
    #plt.legend(loc='best')
    plt.axis([0,16281,0,1])
    #plt.show()
    plt.savefig('education-num.jpg')

def draw_hours_per_week():
    plt.figure(figsize=(10,9))
    plt.title("Hours-per-week table") 
    plt.xlabel("x axis caption") 
    plt.ylabel("y axis caption") 
    for i in range(16281):
        plt.plot(i,dr.datas[i].hours_per_week,'.',) 
    #plt.legend(loc='best')
    plt.axis([0,16281,0,1])
    #plt.show()
    plt.savefig('hours-per-week.jpg')

def remake():
    draw_age()
    draw_fnlwgt()
    draw_education_num()
    draw_hours_per_week()

#tr窗口创建
root = tr.Tk()
root.title("Project 3")
root.geometry('1080x960')


canvas1 = tr.Canvas(root, height=960, width=1080)
img_age = Image.open('age.jpg')  # 打开图片
photo_age = ImageTk.PhotoImage(img_age)  # 用PIL模块的PhotoImage打开
image_age = canvas1.create_image(540, 0, anchor='n',image=photo_age)        # 图片锚定点（n图片顶端的中间点位置）放在画布（540,0）坐标处

canvas2 = tr.Canvas(root, height=960, width=1080)
img_fnlwgt = Image.open('fnlwgt.jpg')  # 打开图片
photo_fnlwgt = ImageTk.PhotoImage(img_fnlwgt)  # 用PIL模块的PhotoImage打开
image_fnlwgt = canvas2.create_image(540, 0, anchor='n',image=photo_fnlwgt)        # 图片锚定点（n图片顶端的中间点位置）放在画布（540,0）坐标处

canvas3 = tr.Canvas(root, height=960, width=1080)
img_education_num = Image.open('education-num.jpg')  # 打开图片
photo_education_num = ImageTk.PhotoImage(img_education_num)  # 用PIL模块的PhotoImage打开
image_education_num = canvas3.create_image(540, 0, anchor='n',image=photo_education_num)        # 图片锚定点（n图片顶端的中间点位置）放在画布（540,0）坐标处

canvas4 = tr.Canvas(root, height=960, width=1080)
img_hours_per_week = Image.open('hours-per-week.jpg')  # 打开图片
photo_hours_per_week = ImageTk.PhotoImage(img_hours_per_week)  # 用PIL模块的PhotoImage打开
image_hours_per_week = canvas4.create_image(540, 0, anchor='n',image=photo_hours_per_week)        # 图片锚定点（n图片顶端的中间点位置）放在画布（540,0）坐标处

on_hit1 = False
def hit_me_1():
    global on_hit1
    if on_hit1 == False:
        on_hit1 = True
        canvas1.pack()
    else:
        on_hit1 = False
        canvas1.pack_forget()

on_hit2 = False
def hit_me_2():
    global on_hit2
    if on_hit2 == False:
        on_hit2 = True
        canvas2.pack()
    else:
        on_hit2 = False
        canvas2.pack_forget()

on_hit3 = False
def hit_me_3():
    global on_hit3
    if on_hit3 == False:
        on_hit3 = True
        canvas3.pack()
    else:
        on_hit3 = False
        canvas3.pack_forget()

on_hit4 = False
def hit_me_4():
    global on_hit4
    if on_hit4 == False:
        on_hit4 = True
        canvas4.pack()
    else:
        on_hit4 = False
        canvas4.pack_forget()

b1 = tr.Button(root, text='Age',command=hit_me_1)
b1.place(x=50, y=10, anchor='nw')
b2 = tr.Button(root, text='Fnlwgt',command=hit_me_2)
b2.place(x=120, y=10, anchor='nw')
b3 = tr.Button(root, text='Education-num',command=hit_me_3)
b3.place(x=220, y=10, anchor='nw')
b4 = tr.Button(root, text='Hours-per-week',command=hit_me_4)
b4.place(x=390, y=10, anchor='nw')
b5 = tr.Button(root, text='remake',command=remake)
b5.place(x=1000, y=10, anchor='nw')

root.mainloop()  # 进入消息循环





