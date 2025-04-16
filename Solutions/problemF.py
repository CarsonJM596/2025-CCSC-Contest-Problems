cup = int(input().strip())
kettle = int(input().strip())
initial_temp = int(input().strip()) #Initial temperature
rate = int(input().strip())
desired_temp = int(input().strip()) #Desired temperature.  Initial temp doesn't matter.
interval = int(input().strip())

prev_time = 0
ncups = 0
temp = max(initial_temp,desired_temp) - rate * interval/kettle

while True:
    t = prev_time + interval

    boiling_time = prev_time + (100 - temp) * kettle / rate

    if t >= boiling_time:
        kettle -= (rate * (t - boiling_time))/540
        temp = 100
    else:
        temp += rate * (t - prev_time)/kettle

    if kettle < cup:
        break

    kettle -= cup
    ncups += 1
    prev_time = t

print(ncups)