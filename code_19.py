#Accept a number and check if it a perfect number or not. A number whose sum of factors is equal to the number itself


num=int(input("enter a number"))
sum=0
for i in range(1,num):
    if(num%i==0):
        sum=sum+i
if(num==sum):
    print(f"{num} is a perfect number")
else:
    print("it is not a perfect number")