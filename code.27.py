def pallindrome(st):#parameeter
    rev = ""
    for i in range(len(st)-1,-1,-1):
        rev = rev+st[i]
    if rev ==st:
        print("palendrome")
    else:
        print("not a palendrome")
        