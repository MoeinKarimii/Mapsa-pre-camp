message = "Babak Korramdin"

# Question A
print(message[0])

# Question B
print(message[6])

# Question C
name = message.split()
print (name[0])
print(name[1])

# Question D
print(message[:12:2])

# Question F
for i in range(len(message)):
    if message[i] == "m":
        print(True)
        break