def max_or_min(num1, num2, num3):
    num_list = [num1, num2, num3]
    max_num = num_list[0]
    min_num = num_list[0]
    for i in range(1,3):
        if num_list[i] > max_num:
            max_num = num_list[i]
        elif num_list[i] < min_num:
            min_num = num_list[i]
    return [max_num, min_num]


final_result = max_or_min(int(input()), int(input()), int(input()))
print(f"Max is: {final_result[0]}")
print(f"Min is: {final_result[1]}")