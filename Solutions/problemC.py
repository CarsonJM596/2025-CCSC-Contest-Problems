import math

d = int(input().strip())
a = int(input().strip())

# d *tan(a in radians) + 1

print(int(round(d * math.tan(a * math.pi / 180) + 1.5))) # +.5 to round up