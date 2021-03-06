def find(f,p,s):
    p -= 1
    for i in range(n):
        if i==f or tbl[f][i]==11:
            continue
        if(p>0):
            find(i,p,s+tbl[f][i])
        else:
            global ans
            ans += tbl[f][i] + s
            print(f"{f} -> {i} = {tbl[f][i]}",ans)

def printtbl():#print tbl
    for i in range(n):
        for j in range(n):
            print(tbl[i][j],end=' ')
        print()

def FWShortestPath():#shortest path for all pair
    global tbl
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if tbl[i][j] > tbl[i][k] + tbl[k][j]:
                    tbl[i][j] = tbl[i][k] + tbl[k][j]
t = int(input())
for case in range(t):
    s = input()
    s = s.split()
    n = int(s[0])
    m = int(s[1])
    p = int(s[2])
    tbl = []
    for i in range(n):
        tbl.append([])
        for j in range(n):
            tbl[i].append(11)
    for i in range(n):
        tbl[i][i] = 0
    for i in range(m):
        s = input().split()
        u = int(s[0])
        v = int(s[1])
        d = int(s[2])
        tbl[u-1][v-1] = d
        tbl[v-1][u-1] = d
    FWShortestPath()
    ans = 0
    find(0,p,0)
    #printtbl()
    print("Case #{}: {:.6f}".format(case+1,ans/(n-1)**p))
