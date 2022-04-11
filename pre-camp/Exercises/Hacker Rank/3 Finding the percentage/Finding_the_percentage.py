roundes = int(input())
values = {}
for i in range(roundes):
    input_list = input().split()
    values.update({input_list[0]: input_list[1:]})
avg_name = input()
avg_score = 0
for i in range(len(values[avg_name])):
    avg_score += float(values[avg_name][i])
avg_score = str(avg_score / len(values[avg_name]))
if len(avg_score) != 5:
    if len(avg_score) == 4 or len(avg_score) == 3:
        avg_score = avg_score + "0"
    elif len(avg_score) > 5:
        avg_score = avg_score[:5]
print(avg_score)

