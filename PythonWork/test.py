from joblib import PrintTime
from sympy import li


print('Hello')
a=0
print (a)
print (type (a))
b = "Hello World"
print (b)
print(type(b))
c="'안녕하세요'"
print(c)
d="\'안녕하세요\'"
print(d)
print(b+c)
print(b)
print(b[0])
print(b[-1])
e = '안녕하세요'
print(e[0:2])
print(e[0:5:2])
print(e[:])
# 주석
#list
l = list()
print (l,type(l))
l = [0,1,2,3,4,5,6,7,8,9,10]
print(len(l))
l.append(999)
l.remove(5)
print(l)
l[1]=[1,2,3]
l[2] = '문자'
print(l)

#tuple==list(단,수정 불가)
t=tuple()
print(t,type(t))
t1=(1,2,3)
print(t1,type(t1))
print(t1[0],t1[0:2])
print(t1+t1)

#dict
d = dict()
print(d,type(d))
d= {
    'a' : 1,
    'b' : 2,
    'c' : 3
}
print(d,type(d))
print(d['a'])
d['c']=33
print(d)
d1 = d.keys()
print("d1:",d1)
d2 = d.items()
print("d2:",d2)
d3 = d.values()
print("d3:",d3)

a = 2
if(a==1):
    print(1)
elif(a==2):
    print(2)
else:
    print("1 아님")

for i in[1,2,3]:
    print(i)

for i in(1,2,3):
    print(i)

for i in "Hello":
    print(i)

num = 5
while(num > 0):
    print(num)
    num -= 1

num = 10
while(num > 0):
    if(num == 6):
        print('----end----')
        break
    print(num,end=' ')
    num -= 1

for i in [1,2,3,4,5,6,7,8,9,10]:
    print(i,end=' ')
print()

for i in range(10):
    print(i,end=' ')
print()

hap = 0
for i in range(101):
    if (i%7 == 0):
        hap =+ i
        print(i,end=' ')
print("\nhap : ",hap)
print()

for i in range(3):
    for j in range(3):
        print ('*',end='')
    print('')

