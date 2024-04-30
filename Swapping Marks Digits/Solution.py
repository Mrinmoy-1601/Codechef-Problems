def rev(num):
    x = num%10
    y = num//10
    n_rev = x*10+y
    return n_rev
n = int(input())
for i in range(n):
    a,b = map(int,input().split(' '))
    print('yes') if a>b or a>rev(b) or rev(a)>rev(b) or rev(a)>b else print('No')
