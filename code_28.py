# num = [10,20,30,40,70,60,50]
# print(len(num)) #len function
# print(max(num)) #max function
# print(min(num)) #min() function
# print(sum(num)) #sum() fuction
# print(list(num))
# print(sorted(num))

# print(num)
# for i in range(len(num)):
#     #print(i) its give you the index
#     print(num[i])
    

# #second way to print the values 
# for i in num:
#     print(num)

# print(dir(list))
# print(list)
# help(list)
# l=[1,2,4,5,2,6,7]
# # l.append(2)#use to add a single value
# # # l.insert(2,3)#use to add value in a specific position
# # # print(l)
# # l.extend([8,9,10,11])#use for adding multiple element at the end
# # print(l)
# v=l.remove(2) #it remove the first occurance of the list
# v1=l.pop(1)
# # print(l)
# # print(3)
# print(v)
# print(v1)

# l=[10,20,30,40,50,60,70]
# l[0]=1
# print(l)

# l=[-45,67,12,-68,-69,34]
# for i in l:
#     if i>=0:
#         print(i)

# a=(1,2,3,3,4,5,6,"bibhu",print("hello"))
# print(type(a))
# print(a)
# print(a[0])
# print(a[2])

# for i in range(len(a)):
#     print(a[i])
    
# for i in a:
#     print(i)
# print(a.index(5))
# print(a.count(3))
# a,b,c,d=(91,2,3,4,)
# print(a)
# print(b)
# print(c)
# print(type(a))
# s={}
# print(type(s))
# s={1,2,3,4,5,6,5,4}
# print(s)
# set([0])
# b=hash("bibhu")
# print(b)
# a={8,1,2,16,3,4,5,6,'hello'}
# for i in range(len(a)):
#     print(a[i])
# for i in a:
#     print(i)
# a.remove(2)
# a.pop()
# print(a)
# a.clear()
# print(a)

a={1,2,3,4,5,6}
b={5,6,7,8,9}
print(a|b)
print(b|a)
print(a&b)
print(b&a)
s=a.union(b)
print(s)