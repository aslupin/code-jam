def ks(a):
#    print(a)
    if len(a) <= 1:
        return a
    b = list()
    c = list()
    rp = (len(a)-1)/2
#    print(rp)
    p = a[int(rp)]
    for i in range(int(rp)):
#        print("F open ",a[i])
        if a[i]<=p:
            b.append(a[i])
        else:
            c.append(a[i])
    for i in range(int(rp)+1,len(a)):
#        print("S open ",a[i])
        if a[i]<=p:
            b.append(a[i])
        else:
            c.append(a[i])
    lp = [p]
#    print("b = ",b,"\nc = ",c)
    if len(b) != 0 and len(c) != 0:
        global wp
        wp = False
    return ks(b) + lp +ks(c)
t = int(input())
for i in range(t):
    wp = True
    j = int(input())
    s = input()
    ks(s.split())
    if wp:
        print("Case #{}: YES".format(i+1))
    else:
        print("Case #{}: NO".format(i+1))
