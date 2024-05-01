t = int(input())
for i in range(t):
    n = int(input())
    b = input()
    if n==1:
        print(0)
    else:
        lst = list(b)
        s=0
        for i in range(1,len(lst)):
            if lst[i]==lst[i-1]:
                s+=1
        print(s)
