def even_number_counter():
    counter = 1
    numbers_list = []
    while counter < 100:
        if counter % 2 == 0:
            numbers_list.append(counter)
        counter += 1
    return numbers_list


def printer(numbers):
    for i in range(len(numbers)):
        print(numbers[i])


printer(even_number_counter())