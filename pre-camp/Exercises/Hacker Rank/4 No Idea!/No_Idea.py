n, m = map(int, input().split())
array = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))
sum_A = 0
for i in array:
    if i in A:
        sum_A += 1
    elif i in B:
        sum_A -=1
print(sum_A)
