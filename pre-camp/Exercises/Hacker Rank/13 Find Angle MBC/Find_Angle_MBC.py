import math

AB = int(input())
BC = int(input())
AC = math.sqrt(AB**2+BC**2)
x = round(math.degrees(math.acos(BC/AC)))
print(str(x)+chr(176))
