def date_to_int(date_parts):
    return int(date_parts[2]) * 10000 + int(date_parts[0]) * 100 + int(date_parts[1])

def parse_person():
    name = input().strip()
    parent1 = input().strip()
    parent2 = input().strip()
    dates = input().strip()
    date_parts = dates.split()
    born = date_to_int(date_parts[:3])
    died = date_to_int(date_parts[3:])
    return name, parent1, parent2, born, died

def max_independent_set(people):
    if len(people) == 0:
        return 0

    people.sort(key=lambda x: x[4])

    dp = [0] * len(people)
    for i in range(len(people)):
        dp[i] = 1 if i == 0 else dp[i-1]
        for j in range(i): #Can be done in log n time with binary search
            if people[j][4] <= people[i][3]:
                dp[i] = max(dp[i],dp[j] + 1)
            else:
                break

    return dp[-1]

def mongogram(name):
    parts = name.split()
    return "".join(part[0] for part in parts)

n = int(input().strip())

people = []
for i in range(n):
    people.append(parse_person())

target = input().strip()

target_person = [p for p in people if p[0] == target]
if len(target_person) == 0:
    ans = 0
else:
    target_person = target_person[0]
    born_later = [p for p in people if p[3] >= target_person[4]]
    ans = max_independent_set(born_later)

print(mongogram(target),ans)