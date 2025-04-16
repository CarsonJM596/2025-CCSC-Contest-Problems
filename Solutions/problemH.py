composite = [False] * 10001

for i in range(2,10001):
    if not composite[i]:
        for j in range(2*i,10001,i):
            composite[j] = True

n = int(input().strip())

t = 0
for i in range(2,n):
    if not composite[i]:
        t += 1

print(f"Jack forgot there are {t} prime numbers less than {n}.")