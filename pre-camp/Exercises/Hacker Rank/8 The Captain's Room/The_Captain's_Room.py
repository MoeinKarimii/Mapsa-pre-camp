k = int(input())
members = list(map(int, input().strip().split()))
members.sort()
members.append([]*k)
i = 0
while i < len(members):
    if members[i] == members[i+1]:
        i += k
        continue
    elif members[i] != members[i+1]:
        print(members[i])
        break
