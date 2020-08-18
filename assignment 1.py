a=2
b=3
print(a+b)

x= int(input("enter number"))
fact= 1
for i in range(1,x+1):
    fact=fact*i
print(fact)

p= 200
r= 2
t= 3
si= float(p*r*t/100)
total= si+p
print(total)
ci= float(p*(1+r/100)**t)
print(ci)

from math import pi
r= int(input("enter number"))
area= float(pi*r**2)
print(area)

s= input("enter armstrong number ")
#n= int(s[0])**3 + int(s[1])**3 + int(s[2])**3
n=0
for i in s:
    n= n+int(i)**len(s)
if int(s) == n:
    print("armstrong")
else:
    print("not armstrong")

c= int(input("enter number"))
count= 0
for i in range(2,c+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)



d= int(input("enter number"))
count= 0
for i in range(1,d+1):
    if d%i==o:
        count=count+1
if count==2:
    print("prime")
else:
    print("not prime")