# %%
file = open('input/input.txt', 'r')
lines = file.readlines()

# %%
# list with tuples
disk_storage = []

# %%
def print_disk():
    line = ""
    for t in disk_storage:
        for i in range(t[1]):
            if t[0] == -1:
                line += '.'
            else:
                line += str(t[0])
    print(line)

# %%

for line in lines:
    for i, c in enumerate(line.strip()):
        if i % 2 == 0:
            disk_storage.append((i//2,int(c)))
        else:
            disk_storage.append((-1,int(c)))
#print_disk()

# %% [markdown]
# ### Part B:

# %%
def get_index_of_next_free_space(count, file_idx):
    idx_list = []
    for i,t in enumerate(disk_storage):
        if i >= file_idx:
            return idx_list
        elif t[0] == -1 and t[1] >= count:
            idx_list.append(i)
    return idx_list

# %%
# compact the files
entries = reversed(disk_storage.copy())
for last_entry in entries:
    if last_entry[0] == -1:
        continue
    else:
        file_idx = disk_storage.index(last_entry)
        idx_list = get_index_of_next_free_space(last_entry[1], file_idx)
        for idx_of_next_free_space in idx_list:
            next_free_space = disk_storage[idx_of_next_free_space]
            if last_entry[1] < next_free_space[1]: 
                disk_storage[idx_of_next_free_space] = (-1,next_free_space[1]-last_entry[1])
                disk_storage.insert(idx_of_next_free_space, last_entry)
                disk_storage[file_idx+1] = (-1, last_entry[1])
                break
            elif last_entry[1] == next_free_space[1]: 
                disk_storage[idx_of_next_free_space] = last_entry
                disk_storage[file_idx] = (-1, last_entry[1])
                break
            else:
                continue
    #print_disk()

# %%
# compute checksum
check_sum = 0
idx = 0
for entry in disk_storage:
    if entry[0] > -1:
        check_sum += sum(range(idx,idx+entry[1],1))*entry[0]
        idx += entry[1]
    else:
        idx += entry[1]
print(check_sum)

