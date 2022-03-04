def shape(length, height):
    height -= 1
    print((height * " ") + (length * "*"))
    for i in range(height - 1):
        height -= 1
        print((" " * height) + "*" + (" " * (length - 2) + "*"))
    print(length * "*")


shape(int(input("length: ")), int(input("height: ")))