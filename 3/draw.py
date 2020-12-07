import pandas as pd
import csv
import numpy as np
f = open('data for project 3.csv','r')

def check(a_string):
    if a_string[-1]=="?":
        return "NaN"
    return a_string

age_min=np.infty
age_max=-np.infty
fnl_min=np.infty
fnl_max=-np.infty
edu_n_min=np.infty
edu_n_max=-np.infty
hpw_min=np.infty
hpw_max=-np.infty

class Data(object):
    def __init__(self,age,workclass,fnlwgt,education,education_num,marital_status,occupation,relationship,race,sex,hours_per_week,native_country):
        self.age=age
        self.workclass=workclass
        self.fnlwgt=fnlwgt
        self.education=education
        self.education_num=education_num
        self.marital_status=marital_status
        self.occupation=occupation
        self.relationship=relationship
        self.race=race
        self.sex=sex
        self.hours_per_week=hours_per_week
        self.native_country=native_country  
        
datas=[]
f.readline()


for i in range(16281):
    new=f.readline()
    new=new.split(",")
    for j in range(12):
        new[j]=check(new[j].strip())
    new_member=Data(0.0,"",0.0,"",0.0,"","","","","",0.0,"")
    new_member.age=float(new[0])
    new_member.workclass=new[1]
    new_member.fnlwgt=float(new[2])
    new_member.education=new[3]
    new_member.education_num=float(new[4])
    new_member.marital_status=new[5]
    new_member.occupation=new[6]
    new_member.relationship=new[7]
    new_member.race=new[8]
    new_member.sex=new[9]
    new_member.hours_per_week=float(new[10])
    new_member.native_country=new[11]
    datas.append(new_member)
    age_min=min(age_min,new_member.age)
    age_max=max(age_max,new_member.age)
    fnl_min=min(fnl_min,new_member.fnlwgt)
    fnl_max=max(fnl_max,new_member.fnlwgt)
    edu_n_min=min(edu_n_min,new_member.education_num)
    edu_n_max=max(edu_n_max,new_member.education_num)
    hpw_min=min(hpw_min,new_member.hours_per_week)
    hpw_max=max(hpw_max,new_member.hours_per_week)
    #print(new)

for i in datas:
    i.age=(i.age-age_min)/(age_max-age_min)
    i.fnlwgt=(i.fnlwgt-fnl_min)/(fnl_max-fnl_min)
    i.education_num=(i.education_num-edu_n_min)/(edu_n_max-edu_n_min)
    i.hours_per_week=(i.hours_per_week-hpw_min)/(hpw_max-hpw_min)
    #print(i.age)

if __name__ == "__main__":
    
    print(fnl_max)