'''
sum1= 0
while True:
    num1=int(input("Enter a Number to be added\n"))
    sum1 = sum1+num1;
    if num1==0:
        break
    print("Current sum is ", sum1)
'''





'''
i = 1
sum1= 0
while i<=10:
    sum1=sum1+i
    print(i, "-->", sum1)
    i=i+1
print(sum1)    
'''




list1 = [10,20,30,40,50,60]
sum1=0
for each in list1:
    if sum1 >= 100:
        break
    sum1 = sum1+each
    print(each)

print("Sum is ", sum1)
