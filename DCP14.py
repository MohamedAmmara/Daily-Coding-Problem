#The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.

#Hint: The basic equation of a circle is x2 + y2 = r2.

import random
lst=[]
n=10000000
num=0
for i in range(n):
    lst.append([random.random(), random.random()])
for i in lst:
    if i[0]**2+i[1]**2<=1:
        num+=1
print(num*4/n)
