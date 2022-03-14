num_list = [1, 8, 12, 9, 1, 5 ,12, 21, 3, 4, 9, 2, 5]
progress = []
for i in range(len(num_list)):
    if i == 0:
        pass
    elif num_list[i] > num_list[i-1]:
        progress.append(True)
    else:
        progress.append(False)
print(progress)
counter = []

for i in range(1, len(progress)):
    if progress[i] != progress[i-1]:
        counter.append(i)
print(counter)