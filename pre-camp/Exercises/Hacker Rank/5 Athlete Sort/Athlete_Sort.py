nm = input().split()
n = int(nm[0])
m = int(nm[1])
arr = []
arr1 = []
for _ in range(n):
    a = input()
    arr.append(list(map(int, a.rstrip().split())))
    arr1.append(list(a.strip().split()))    
k = int(input())
sort_list = []
for i in range(n):
    sort_list.append(arr[i][k])
sort_list.sort()
result = []
for i in range(n):
    result.append([])
    for j in range(n):
        if sort_list[i] == arr[j][k]:
            result[i].append(arr1[j])
            break
for i in range(n):
    print(" ".join(result[i][0]))
