#coding:utf8
import math 

"""n=0
for i in range(1,7,1):
    x=(1/4)*((i/8)**2)
    n+=x
print(n)"""

"""x_i=0
for i in range (1,100000000,1):
    x=(1/100000000)*((i/100000000)**3)
    x_i+=x
print(x_i)"""

x_i=0
for i in range (1,1000000,1):
    x=(math.pi/2000000)*(math.cos((math.pi/2000000)*i))
    x_i+=x
print(x_i)