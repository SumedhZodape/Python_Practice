'''
num1 = int(input("Enter the Number:"))
num1_sq=int(num1**.5)+1
flag=0

for each in range (2, num1_sq+1):
    if num1%each ==0:
        print("Number is not prime")
        flag=1
        break


if flag == 0:
    print("Number is prime")
'''





# using for else statement

num1 = int(input("Enter the Number\:n"))
num1_sq = int(num1**.5)+1

for each in range(2, num1_sq+1):
    if num1%each ==0:
        print("Number is not prime")
        break
else:
    print("Number is prime")    
