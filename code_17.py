
#print the sum of all even num and odd num separat
num=int(input("enter a number"))
odd=0
even=0
for i in range(1,num+1):
    if(i%2==0):
        even=even+i
    else:
        odd=odd+i
        
print("the sum of even numbr is :",even)
print("the sum of odd number is :",odd)