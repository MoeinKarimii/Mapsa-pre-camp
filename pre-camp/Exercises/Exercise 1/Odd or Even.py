def odd_or_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


if odd_or_even(int(input())):
    print("The number is EVEN")
else:
    print("The number is ODD")