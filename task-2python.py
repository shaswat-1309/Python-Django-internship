#single line comment
'''triple
line
comment'''

#variables

n1=7
n2=4.6
name = "shaswat"

print(n1)
print("n2 is ",n2)
print("My name is ",name)

#changing the value of variable

name = "i am doing python internship"
print(name)

#declaring variables in singleline

a,b,c = 10,6.7,"hello world"
d=e=4
print("Value of a is ",a)
print("Value of b is ",b)
print("Value of c is ",c)
print("Value of d is ",d)
print("Value of e is ",e)

#datatypes in python

#numbers

print(type(a))
print(n2,"is complex number?",isinstance(10.5,int))

#string datatype

name="shaswat"
print("name is:",name)

print("First Character of string is",name[0])

print("Characters from 3rd to 6th",name[3:6])

print("only starting value",name[0:])

print("only ending value",name[:5])

print("Two times",name*2)

#List datatype

l1 = [4,4.5,"shaswat",7]
print(l1)

print("type of l1",type(l1))
print("l1[2]",l1[2])

print("l1[0:2]",l1[0:2])

#tuple datatype

t1=(10,20,30,"hello",40,"world")

print(t1)

print("type of t1",type(t1))
print("t1[4]",t1[4])

print("t1[0:5]",t1[0:5])

#dictionary datatype

d1={1:"hello", a:"world", 'name':"shaswat", 2:5,}

print(d1)

print("type of d1",type(d1))
print("d1[4]",d1[2])

print("d1[1]",d1[1])
