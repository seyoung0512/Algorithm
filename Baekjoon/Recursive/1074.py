def dac(n,r,c,q=None):
    global cnt
    if n == 1:
        if (r,c) == (0,0):
            q = 0
        elif (r,c) == (0,1):
            q = 1
        elif (r,c) == (1,0):
            q = 2
        else:
            q = 3
        cnt += q
        print(cnt)
    else:
        if r >= 2**(n-1) and c >= 2**(n-1):
            r -= 2**(n-1)
            c -= 2**(n-1)
            q = 3
            cnt += q * 2 ** (n-1) * 2 ** (n-1)
        elif r >= 2**(n-1) and c < 2**(n-1):
            r -= 2**(n-1)
            q = 2
            cnt += q * 2 ** (n-1) * 2 ** (n-1)
        elif r < 2**(n-1) and c >= 2**(n-1):
            c -= 2**(n-1)
            q = 1
            cnt += q * 2 ** (n-1) * 2 ** (n-1)
        else:
            q = 0
        # print(n,r,c,q,cnt)
        dac(n-1,r,c,q)

n, r, c = map(int, input().split())
cnt = 0
# print(n, r, c, cnt)
dac(n,r,c)

