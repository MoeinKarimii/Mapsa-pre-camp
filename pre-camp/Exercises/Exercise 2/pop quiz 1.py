num_list = [1, 2, 3, 8, 9, 21, 12, 15, 18, 42]
progress = []
for i in range(len(num_list)):
    if i == 0:
        pass
    elif num_list[i] > num_list[i-1]:
        progress.append(True)
    else:
        progress.append(False)
print(progress)
counter = 0
for i in range(1, len(progress)):
    if progress[i] == progress[i-1]:
        counter +=1
print(counter)