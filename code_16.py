#factorial of a number
num=int(input("enter a number"))
facto=1
for i in range(1,num+1):
    facto=facto*i
print(facto)