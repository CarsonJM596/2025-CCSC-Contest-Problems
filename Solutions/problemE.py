from collections import Counter

n = int(input().strip())

def normalize(s):
    return ''.join(c for c in s.lower() if c.isalpha())

for i in range(n):
    words = input().split()
    words = [normalize(w) for w in words]
    counts = Counter(words)
    highest = max(counts.values())
    best_words =[]
    for word, count in counts.items():
        if count == highest:
            best_words.append(word)
    if len(best_words) == 1:
        print(best_words[0], highest)
    else:
        print("(many)", highest)