string_list = list(input())
counter = 0
for i in range(len(string_list)):
    if string_list.count("?") == len(string_list) and string_list[i] != "?":
        break
    if string_list.count("?") == len(string_list) and string_list[i] == "?":
        if string_list[i-1] == "0":
            string_list.pop(i)
            string_list.insert(i, "1")
        elif string_list[i-1] == "1":
            string_list.pop(i)
            string_list.insert(i, "0")
    if i == len(string_list)-1:
        if string_list[i] == string_list[i-1]:
            print(False)
            counter += 1
            break
    elif string_list[i] == "0" and i < len(string_list)-1:
        if string_list[i+1] == "0":
            print(False)
            counter += 1
            break
        else:
            continue
    elif string_list[i] == "1" and i < len(string_list)-1:
        if string_list[i+1] == "1":
            print(False)
            counter += 1
            break
        else:
            continue
    elif string_list[i] == "?":
        if i == 0:
            if string_list[i+1] != "?":
                if string_list[i+1] == "0":
                    string_list.pop(i)

        elif string_list[i-1] == "0":
            string_list.pop(i)
            string_list.insert(i, "1")
        elif string_list[i-1] == "1":
            string_list.pop(i)
            string_list.insert(i, "0")
                    
print(string_list)
if counter == 0:
    print(True)