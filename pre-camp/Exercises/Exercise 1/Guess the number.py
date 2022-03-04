import random
number = random.randint(1, 20)
for i in range(5):
    guess_num = int(input("Enter Your Number: "))
    if guess_num == number:
        print("You Win")
        exit()
print(f"The Number was {number}")
print("Game Over")