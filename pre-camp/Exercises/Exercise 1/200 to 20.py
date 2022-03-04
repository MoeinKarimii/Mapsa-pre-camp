def number_picker():
    for i in range(200, 20, -1):
        if i % 5 == 0:
            if i % 3 == 0:
                continue
            print(i)


number_picker()