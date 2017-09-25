def ks(a):
    lenS = len(a)
    for i in range(lenS):
        a[i] = int(a[i])
    b = sorted(a)
    mn = b[0]
    imn = 0
    mx = b[len(b)-1]
    imx = len(b)-1
    px = 0
    pn = 0
    while a:
        p = a.pop((len(a)-1)//2)
#        print("cut",p)
        if p == mx:
            px += 1
            imx -= 1
            mx = b[imx]
        elif p == mn:
            pn += 1
            imn += 1
            mn = b[imn]
    if lenS == px + pn:
        return True
    return False
t = int(input())
for i in range(t):
    j = int(input())
    s = input()
    wp = ks(s.split())
    if wp:
        print("Case #{}: YES".format(i+1))
    else:
        print("Case #{}: NO".format(i+1))
