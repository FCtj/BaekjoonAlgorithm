import sys

N = int(sys.stdin.readline())
count = [0] * 8001
abs_value = 4000
inputs = [int(sys.stdin.readline()) for i in range(N)]

inputs.sort()

total = 0
max_count = 0
for i in inputs:
    total += i
    count[i+abs_value] += 1
    if count[i+abs_value] > max_count:
        max_count = count[i+abs_value]

is_second = False
fre_count = 0
for i in range(8001):
    if count[i] == max_count:
        fre_count = i - abs_value
        if is_second:
            break
        is_second = True
avg = total / len(inputs)
if avg <0:
    avg = int(avg - 0.5)
else:
    avg = int(avg + 0.5)
mid = inputs[(len(inputs)-1)//2]

minx = inputs[0]
maxx = inputs[-1]
rangex = maxx - minx    

answer = [avg,mid,fre_count,rangex]
for i in answer:
    print(i)
