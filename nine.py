n=3
ch='a'
for i in range(n):
    for j in range(n):
        print(ch,end='')
        ch=chr(ord(ch)+1)
    print()