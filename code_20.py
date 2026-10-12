# Check wether the number is prime or not 
num=int(input("enter a number"))
for i in range(2,num):
    if(num%i==0):
        print(f"{num} is not a prime number")
    else:
        print(f"{num} is a prime number")