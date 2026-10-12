n=5
ch='a'
for i in range(n):
    for j in range(i+1):
        print(ch,end=' ')
        
    print()
    ch=chr(ord(ch)+1)