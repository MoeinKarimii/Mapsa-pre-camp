number = list(input())
result_list = []
for i in range(len(number)-1):
    hypothetical_list = number.copy()
    sum = (int(hypothetical_list.pop(i)) + int(hypothetical_list.pop(i)))
    hypothetical_list.insert(i, str(sum))
    result_list.append(int("".join(hypothetical_list)))
print(max(result_list))