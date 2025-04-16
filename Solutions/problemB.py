from collections import Counter

l  = input()

frequency = Counter(l)

to_return = 1
for c in frequency:
    if c.isalnum():
        to_return *= frequency[c]

print(to_return % (10**9 + 7))