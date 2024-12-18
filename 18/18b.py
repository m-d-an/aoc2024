# %%
example = False

# %%
if example:
    file = open('input/example.txt', 'r')
else:
    file = open('input/input.txt', 'r')
lines = file.readlines()

# %%
if example:
    max_x = 7
    max_y = 7
    number = 12
else:
    max_x = 71
    max_y = 71
    number = 1024

# %%
def print_grid(positions):
    for y in range(max_y):
        line = ""
        for x in range(max_x):
            if (x,y) in positions:
                line += '#'
            else:
                line += '.'
        print(line)

# %% [markdown]
# ### Part A:

# %%
start = (0,0)
end = (max_x-1,max_y-1)
move = [(-1,0),(1,0),(0,-1),(0,1)]

# %%
def find_path(blocks):
    visited_steps = {start: 0}
    to_visit = [start]

    while len(to_visit) > 0:
        # next tile with shortest distance
        tile = to_visit[0]
        for node in to_visit:
            if visited_steps[node] < visited_steps[tile]:
                tile = node

        # check neighbours
        for m in move:
            neighbour = (tile[0]+m[0],tile[1]+m[1])
            if neighbour[0] < 0 or neighbour[1] < 0 or neighbour[0] >= max_x or neighbour[1] >= max_y:
                continue
            elif neighbour in blocks:
                continue
            else:
                distance = visited_steps[tile] + 1
                if not (neighbour in visited_steps) or distance < visited_steps[neighbour]:
                    visited_steps[neighbour] = distance
                    to_visit.append(neighbour)
        # remove current tile
        to_visit.remove(tile)

    if end in visited_steps:
        return True
    else:
        return False

# %%
blocks = []
for i in range(number, len(lines), 1):
    blocks = []
    for line in lines[:i]:
        coords = line.strip().split(',')
        blocks.append((int(coords[0]),int(coords[1])))
    if not find_path(blocks):
        print(i, lines[i-1])
        #print_grid(blocks)
        break


