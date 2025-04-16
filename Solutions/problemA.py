n = int(input().strip())

# Given a complete last row r, there are r * (r+1) / 2 ants
# So solve for r * (r+1) / 2 = n
# r^2 + r - 2n = 0
# r = (-1 + sqrt(1 + 8n)) / 2

r = int((-1 + (1 + 8 * n) ** 0.5) / 2)

to_return = int(n - r * (r+1) / 2)
if to_return == 0:
    to_return = r
print(to_return)