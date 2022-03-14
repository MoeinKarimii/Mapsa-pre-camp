def find(num1, num2, num3):
    num_list = [num1, num2, num3]
    for i in range(1, 5):
        if i in num_list:
            continue
        return i


print(find(int(input()), int(input()), int(input())))