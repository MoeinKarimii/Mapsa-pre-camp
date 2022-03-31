while True:
    rounds = int(input())
    num_list = list(input())
    counter = 0
    for i in range(len(num_list)):
        num_list[i] = int(num_list[i])
    orgin_list = num_list.copy()
    for i in range(1, len(num_list)-1):
        while num_list[i] > num_list[i-1] and num_list[i] > num_list[i+1]:
            if num_list[i-1] != orgin_list[i-1]:
                num_list[i-1] += 1
            else:
                num_list[i+1] += 1
    for i in range(len(num_list)):
        if num_list[i] != orgin_list[i]:
            counter += 1                
    print(counter)
    print(num_list)