def multiplication():
    for i in range(1, 11):
        number = ""
        for j in range(1, 11):
            number += (str(i * j) + "\t")
        print(number)


multiplication()