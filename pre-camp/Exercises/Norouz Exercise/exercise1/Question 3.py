string_list = list(input())
break_count = 0
if string_list.count("?") == len(string_list):
    print(False)
    break_count +=1 
for i in range(len(string_list)):
    if string_list[i] == "?":
        j = i
        counter = 0
        while string_list[j] == "?":
            counter += 1
            j += 1
        if i == 0:
            check = i
            if counter % 2 == 0:
                string_list[check] = string_list[j]
                continue
            elif counter % 2 != 0:
                if string_list[j] == "0":
                    string_list[check] = "1"
                elif  string_list[j] == "1":
                    string_list[check] = "0"
        elif j == len(string_list):
            check = i
            while check < j:
                if string_list[check-1] == "1":
                    string_list[check] = "0"
                elif string_list[check-1] == "0":
                    string_list[check] = "1" 
                check += 1
        elif (counter % 2 != 0 and string_list[i-1] != string_list[j]) or (counter % 2 == 0 and string_list[i-1] == string_list[j]):
            print(False)
            break_count += 1
        elif (counter % 2 == 0 and string_list[i-1] != string_list[j]) or (counter % 2 != 0 and string_list[i-1] == string_list[j]):
            check = i
            while check < j:
                if string_list[check-1] == "1":
                    string_list[check] = "0"
                elif string_list[check-1] == "0":
                    string_list[check] = "1"
                check +=1
if break_count == 0:
    print(True)
    print(" ".join(string_list))