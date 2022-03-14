def list_checker(list1):
    progress = []
    for i in range(0, len(list1)-1):
        if list1[i] > list1[i+1]:
            progress.append(False)
        elif list1[i] < list1[i+1]:
            progress.append(True)
        if i == 0:
            progress.append(progress[0])
    print(progress)
    i = 2
    indexes = []
    while i < len(progress):
        if progress[i] == progress[i-1] == progress[i-2]:
            i += 1
            continue
        else:
            if progress[i] != progress[i-1]:
                indexes.append(i)
            elif progress[i] != progress[i-2]:
                indexes.append(i-1)
            i += 3
    print(indexes)
    final_lists = []
    co_list = []
    for i in range(len(indexes)):
        if i == 0:
            final_lists.append(list1[0:indexes[i]])
            co_list.append(list1[indexes[-1]:])
        else:
            final_lists.append(list1[indexes[i-1]:indexes[i]])
    final_lists.append(co_list[0])
    return final_lists

def checker(list1, list2):
    ultimate_lists = []
    for k in range(len(list1)):
        y = [x for x in list1[k] if x in list2[k]]
        ultimate_lists.append(y)
    for j in range(len(ultimate_lists)):
        if len(ultimate_lists[j]) == 0:
            ultimate_lists.pop(j)
    return ultimate_lists
    
num_list1 = [1, 3, 8, 12, 24, 2, 15, 16, 21, 3, 4, 67]
num_list2 = [1, 8, 9, 21, 2, 16, 17, 7, 28, 67]
first_list = list_checker(num_list1)
second_list = list_checker(num_list2)
print(first_list)
print(second_list)
print(checker(first_list, second_list))