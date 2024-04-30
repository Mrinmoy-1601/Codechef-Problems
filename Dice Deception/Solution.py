t = int(input())
for i in range(t):
    n,k = map(int,input().split(' '))
    lst = list(map(int,input().split(' ')))
    lst.sort()
    sum1 = sum(lst)
    c = [1,2,3]
    for i in range(k):
        a = lst[0]
        lst.remove(a)
        if a in c:
            sum1 = sum1+7-(2*a)
        else:
            sum1 = sum1
    print(sum1)
