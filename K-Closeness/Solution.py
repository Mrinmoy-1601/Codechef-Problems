t = int(input())
for _ in range(t):
    n,k = map(int,input().split(' '))
    b = list(map(int,input().split(' ')))
    a = []
    for i in range(n):
        a.append(b[i]%k)
    a.sort()
    ans = a[n-1]-a[0]
    c=[]
    for i in range(n-1):
        c.append(a[i]-a[i+1])
    ans=min(min(c)+k,ans)
    print(ans)
