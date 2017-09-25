from math import sqrt
t = int(input())
for i in range(t):
    s = int(input())
    p = 0
    while s>0:
    #    oldS = s
        s -= pow(int(sqrt(s)),2)
        p += 1
    #    print(" eat ",oldS-s)
    print("Case #{}: {}".format(i+1,p))
