t = int(input())
for _ in range(t):
    n,m = map(int,input().split(' '))
    n_s = list(map(int,input().split(' ')))
    m_s = list(map(int,input().split(' ')))
    if (n+m>=11):
        if n>=4 and m>=4:
            n_s.sort(reverse=True)
            m_s.sort(reverse=True)
            n_man = n_s[:4]
            n_re = n_s[4:]
            m_man = m_s[:4]
            m_re = m_s[4:]
            c_re = n_re+m_re
            c_re.sort(reverse = True)
            b_man = c_re[:3]
            s = sum(n_man)+sum(m_man)+sum(b_man)
            print(s)
        else:
            print(-1)
    else:
        print(-1)
