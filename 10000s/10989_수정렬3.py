#Counting sort
import sys
arr = [0] * 10001
N = int(sys.stdin.readline())
for i in range(N):
    arr[int(sys.stdin.readline())] += 1
for i in range(10001):
    while arr[i] != 0:
        print(i)
        arr[i] -= 1
