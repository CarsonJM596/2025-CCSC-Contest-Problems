walls = [[None for _ in range(70)] for _ in range(70)]

n = int(input().strip())

pos = (35,34)
dir = (0,1)
for _ in range(n):
    s = input().strip()

    pos = (pos[0]+dir[0],pos[1]+dir[1]) # In the middle of the cell

    d = s[1]

    if d == 'S':
        #dir = dir
        wall0 = (pos[0]-dir[1],pos[1]+dir[0])
        wall1 = (pos[0]+dir[1],pos[1]-dir[0])
    elif d == 'L':
        wall0 = (pos[0]+dir[1],pos[1]-dir[0])
        dir = (-dir[1],dir[0])
        wall1 = (pos[0]+dir[1],pos[1]-dir[0])
    elif d == 'R':
        wall0 = (pos[0]-dir[1],pos[1]+dir[0])
        dir = (dir[1],-dir[0])
        wall1 = (pos[0]-dir[1],pos[1]+dir[0])

    pos = (pos[0]+dir[0],pos[1]+dir[1])
    if walls[pos[0]][pos[1]]: #Crossing a wall
        print("No")
        exit()


    dirs = [(0,1),(0,-1),(1,0),(-1,0)]
    neighbors = set((pos[0] + di[0],pos[1] + di[1]) for di in dirs)
    others = list(neighbors - set([wall0,wall1]))
    all_walls = [(wall0,s[0]), (wall1,s[2]),(others[0],"0"),(others[1],"0")]

    for wall,s_value in all_walls:
        wall_value = walls[wall[0]][wall[1]]
        s_value = s_value == "1"
        if wall_value is not None and wall_value != s_value:
            print("No")
            exit()
        walls[wall[0]][wall[1]] = s_value

print("Yes")