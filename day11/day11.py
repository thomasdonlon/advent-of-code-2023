with open('day11input.txt', 'r') as f:
	data = f.readlines()

for i, line in enumerate(data):
	data[i] = list(line.strip()) #convert all to lists

#part 1

#record what rows and columns are expanded
expand_rows = []
for i, row in enumerate(data):
	if len(set(row)) == 1: #only contains .
		expand_rows.append(i)

#expand cols, could numpy transpose instead 
expand_cols = []
for j in range(len(data[0])):
	col = []
	for i in range(len(data)):
		col.append(data[i][j])
	if len(set(col)) == 1: #only contains .
		expand_cols.append(j)

#get locations of all galaxies
gal_locs = []
for i in range(len(data)):
	for j in range(len(data[i])):
		if data[i][j] == '#':
			gal_locs.append([i,j])

def additional_expansion(i,j, amount):
	add_exp = 0
	for row in expand_rows:
		if min(gal_locs[i][0], gal_locs[j][0]) < row and max(gal_locs[i][0], gal_locs[j][0]) > row:
			add_exp += amount - 1 #account for original row that was replaced
	for col in expand_cols:
		if min(gal_locs[i][1], gal_locs[j][1]) < col and max(gal_locs[i][1], gal_locs[j][1]) > col:
			add_exp += amount - 1
	return add_exp

#compute manhattan distance between each pair of galaxies
cum_sum = 0
for i, gal1 in enumerate(gal_locs):
	for j, gal2 in enumerate(gal_locs):
		if j > i:
			cum_sum += abs(gal2[0]-gal1[0]) + abs(gal2[1]-gal1[1]) + additional_expansion(i,j,2)

print(f'Total distance between galaxies: {cum_sum}')

#part 2

#compute manhattan distance between each pair of galaxies
cum_sum = 0
for i, gal1 in enumerate(gal_locs):
	for j, gal2 in enumerate(gal_locs):
		if j > i:
			cum_sum += abs(gal2[0]-gal1[0]) + abs(gal2[1]-gal1[1]) + additional_expansion(i,j,1000000)

print(f'Total distance between galaxies: {cum_sum}')