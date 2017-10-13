t = int(input()) # set name your var like process's var
for ti in range(t):
    e,n = input().split()
    e,n = int(e),int(n)
    h = 0
    s = input()
    s = s.split()
    for i in range(len(s)):
        s[i] = int(s[i])
    lis = sorted(s)
    while lis:
        if e > lis[0]:
            h += 1
            e -= lis[0]
            lis.pop(0)
        elif len(lis)>1 and lis[len(lis)-1]+e>lis[0] and h>0:
            e += lis[len(lis)-1] - lis[0]
            lis.pop(len(lis)-1)
            lis.pop(0)
        else:
            break
    print(f"Case #{ti+1}:",h)
