from itertools import combinations

N = int(input())
elements = input().split()
K = int(input())
a = []
num = []
for i in range(N):
    if elements[i] == 'a':
        a.append(i)
    num.append(i)
my_list =  list(combinations(num, K))
sum1 = 0
for i in range(len(my_list)):
    for j in range(len(a)):
        if a[j] in my_list[i]:
            sum1 += 1
            break
print(sum1/len(my_list))
