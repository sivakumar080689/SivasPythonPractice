
#functions

def greet():
    print("Good morning")

greet()


num =4
def getsum(a,b):
    num = a+b
    return num

d = getsum(1,5)
print(d)
print(num)


def myfunc(*args):
    for arg in args:
        print(arg)


myfunc('a','b','c')
myfunc(1,2,3)
myfunc(True,False)


def getsum(a,b):
    num = a+b
    return num


def getsum3(*args):
    print(args,type(args))
    num=0
    for a in args:
        num = num+a
    return num


d=getsum3(1,2,3)
print(d)

def getsum(a,b):
    print(b,type(b))

d= getsum(b=1.0,a=2)



def getsum3(**kwargs):
    print(kwargs,type(kwargs))
    print('name',kwargs['name'])


d=getsum3(id=24,name='rahul',age=35)


a=[1,2,3]
b=[1,2,3,4]

def getmean(a):
    return  sum(a)/len(a)

print(getmean(a))
print(getmean(b)


import os
os.listdir()
import datetime as dt

print(dt.datetime.today().strftime('%Y-%m-%d'))


def getsum3(*args,**kwargs):
    print(args,type(args))
    print(kwargs,type(kwargs))

d=getsum3(1,2,3,a=2,b=2,c=3)



global  c
c=10
def var(a,c):

    c=c+a
    print(c)

var(2,3)
print(c)






