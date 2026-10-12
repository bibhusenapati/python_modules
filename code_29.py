# def greet(name):
#     """return a greeting for name"""
#     return f"hello {name}"

# message=greet("bibhu")
# print(message)
# # n=input("enter your name:")
# # print(greet(n))
# greet("sambita")

#function defination
# def printme(str):
#     "this prints a passed string into this function"
#     print(str)
#     return
# printme("i am first call to the user defined function")
# printme("again second call to the same function")

#parameter the name in the defination and argument the name in the function call

# def greetings(name):
#     "this is docstring of greeting function"
#     print("good morning",name)
#     return
# greetings("bibhu")
# greetings("sambita")
# greetings("binay")

# def sum_of(a,b=70):
#     c=a+b
#     print(c)
#     return
# sum_of(40,6) #positional argument
# sum_of(a=30,b=20) #keyword argument
# sum_of(a=50)

# def add(*args):
#     print(args)
# add(10,20,30,40)

# def add(*args):
#     total=0
#     for i in args:
#         total+=i
#     return total
# print(add(10,20,30))
# print(add(30,40,50,60))

# t=(10,20,30,40,50)
# print(t[1])

# def student(**bibhu):
#     print(bibhu)
# student(name="bibhu",age=21,course="cse")

# def order(item,qty=1,*extras,**details):
#     print(item,qty,extras,details)
# order("tae")
# order("tea",2,"suger","milk",size="large",temp="hot")

# def add(a,b):
#     return a+b
# result=add(a=50,b=90)
# print(result)

# def add(a,b):
#     print(a+b)
# add(10,30)
# x = add(10, 20)
# y = x * 2

# print(y)   

# def add(a,b):
#     return a+b
# x=add(10,30)
# print(x)
# y=x*2
# print(y)

# def greet(name):
#     return f"hello {name}"
# message=greet("bibhu")
# print(message)
# print(message+" what is your name")

# def test():
#     return 10
#     print("Hello")   # ❌ never executes

# print(test())


# total = 0#global variable
# def sum(arg1,arg2):#function defination
#     total=arg1+arg2
#     print("inside the function local total:",total)
#     return total
# sum(10,20)#function call
# print("outside the function global total:",total)

# add=lambda a,b:a+b
# print(add(10,20))
# total=lambda a,b,c:a+b+c
# print(total(10,20,30))

# lambda x:y = x * 2 

def countdown(n):
    if n==0:
        return
    print(n)
    countdown(n-1)

countdown(5)

def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)
print(factorial(5))
