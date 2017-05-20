tc = int(input())

def gcm(M,N):
    if N == 0:
        return M
    else:
        return gcm(N,M%N)

for i in range(tc):
    M,N,x,y = tuple([int(i) for i in input().split()])
    lcm = M*N/gcm(M,N)
    while x != y and x <= lcm:
        if x < y:
            x += M
        else:
            y += N
    if x != y:
        print(-1)
    else:
        print(x)
    
