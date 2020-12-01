#Question 6
import numpy as np 
a = np.zeros(10,dtype=int)
a[4]=1
print(a)

#Question 7
import numpy as np 
a = np.zeros((10,10),dtype=int)
a[1]=1
a[9]=1
for i in range(10):
    a[i,0]=1
    a[i,9]=1
print(a)

#Question 8
import numpy as np 
a = np.array(range(10,30),dtype=int)
a.resize((2,10))
sum1=0
sum2=0
for i in a[0]:
    sum1+=i
for i in a[1]:
    sum2+=i 

#Question 9
import numpy as np 
a = np.zeros([8,8],dtype=int)
qwq=True
for i in a:
    if qwq:
        qwq=False
        i[1]=1
        i[3]=1
        i[5]=1
        i[7]=1
    else:
        qwq=True
        i[0]=1
        i[2]=1
        i[4]=1
        i[6]=1
#print(a)

#Question 10
import numpy as np 
from matplotlib import pyplot as plt 

x = np.arange(0,2.1,0.1) 
y=np.power(np.sin(x-2),2)*np.power(np.e,-1*np.power(x,2))
plt.title("Matplotlib demo") 
plt.xlabel("x axis caption") 
plt.ylabel("y axis caption") 
plt.plot(x,np.power(np.sin(x-2),2)*np.power(np.e,-1*np.power(x,2)),'*b--',label='$sin^2(x-2)* e^{-x^2}  $') 
plt.legend(loc='best')
plt.axis([0,2,0,2])
plt.show()
