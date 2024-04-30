T = int(input())
for i in range (T):
    n,x,y = map(int,input().split(' '))
    lst = []
    a = input()
    lst = a.split(' ')
    for i in range(len(lst)):
        lst[i] = int(lst[i])
    sum = 0
    for i in range(len(lst)):
        if x*lst[i]<y:
            sum+=x*lst[i]
        else:
            sum+=y
    print(sum)
