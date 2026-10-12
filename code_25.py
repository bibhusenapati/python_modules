#for gasing rendom number we have library (rendom)
import random
#to genarate a rendom number
num=random.randint(1,11) #parameter to genarate a num
print(num)
tries = 0
# guess= int(input("enter a number"))
while True:
    guess= int(input("enter a number"))
    if(guess==num):
        tries +=1
        print("you won")
        break
    else:
        tries +=1
        print("you loos")

print(f"the number of tries you make is {tries}")
    
    
    
    
#  if(guess==num):
#     print("you won")
# else:
#     print("you loos")