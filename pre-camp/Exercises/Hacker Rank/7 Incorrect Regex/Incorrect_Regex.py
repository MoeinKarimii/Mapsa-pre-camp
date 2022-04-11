import re
rounds = int(input())
result = []
for i in range(rounds):
    try :
        re.compile(input())
    except re.error:
        print(False)
        continue
    print(True)
