def f(k,n):
    past = [i+1 for i in range(n)]
    for i in range(k):
        cur = []
        for j in range(n):
            if j is 0:
                cur.append(1)
            else:
                cur.append(past[j] + cur[j-1])
        past = cur
    return cur[n-1]

for i in range(int(input()):
    k = int(input())
    n = int(input())
    print(f(k,n))
    
