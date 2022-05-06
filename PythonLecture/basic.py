# a = 10
# print(id(a))



'''
# del
a = 10
print(a)
b=a
print(b)

print(id(a))
print(id(b))

a=20
print(a)
print(id(a))

del(a)
#print(a) #it throw the error becouse it is cutted the linked

print(b)

'''










'''
# Numeric Type

# complex Number
a=9+80j
print(a)
print(a.real)
print(a.imag)
'''


'''
# Exception with immutable Object

# Integer between -5 to 256

# x=50
# y=50
# print(id(x))
# print(id(y))


m=-300
n=-300
print(id(m))
print(id(n))

'''








"""
# string

# Sting is may be or not can be  change

#Both are same 
k = "hello"
b= "hello"
print(id(k))
print(id(b))


#both are same but sir say it is different
l="hello!"
j="hello!"
print(id(l))
print(id(j))
"""





'''
# Operators

print(bin(240))

print(int('11110000', 2))

'''








'''
#Formatted output

txt1= "My Name is {fname}, I'm {age}".format(fname="Sumedh",age=21)
print(txt1)

txt2= "My Name is {}, My age is {}".format("Ssamir", 23)
print(txt2)

txt3= "My name is {} and my age is {}".format("Saurab", 18)
print(txt3)

'''






''''
# Logical Operator

# print(intel > 9 and 7>3) #thro the error

# print(9>60 and 9>intel) #it give false becouse the and operator is checking first condition if it true then check next condition but if first
#conditon is false then interpreter is not checking second conditon


# print(9>3 and 8>intel) #it will throw the error becouse first condition is true then interpreter check second condition


print(5>4 or 8>intel) #it gives true or is only want one condition

print(4>5 8>intel) #its throw the error

'''




'''

# identity operator
a=20
b=20
print(a==b) #true
print(a is b) #false


c=340
d=340
print(c==d)
print(c is d)
print(c is not d)

'''










'''

# print(10 > 7 or 9>3 and 8<3)

# print(2**-1)
# a="10"
# print(type(a))
# b=10
# print(type(b))

# print(id(a))
# print(id(b))
# print(a==b)
# print(a is b)



a="10"
print(type(a))

a = int(a)
print(a, type(a))

'''










'''

# formatted string

fname = "Piyush"
lname="Bansod"
age=23
marks=90.34

# print("%s %s is %d year old and got %f marks"%(fname,lname,age,marks))
print(f"{fname} {lname} is {age} year old boy and got {marks} of marks")

'''




'''

# input function

#input function takes everything as string
# a=input("Enter Your Name\n")
# print(a, type(a))



pwd = input("Enter the password\n")
if pwd == "intel":
    print("Welcome to Hostel")

print("Done")

'''
















