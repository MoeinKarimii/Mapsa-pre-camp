def my_multiple(x, y):
    if y > 1:
        return x + my_multiple(x, y-1)
    return x


print(my_multiple(int(input()), int(input())))