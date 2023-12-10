#there is definitely a lot of room to improve this code by refactoring a lot of the grid traversal stuff into a single function
#but I have already spent way too long on an advent of code so I will not be doing that. Read at your own risk

with open('day10input.txt', 'r') as f:
	data = f.readlines()

#part 1

#don't have to actually implement a path algorithm like A* since each pipe only has an entrance and exit
#the tricky part is getting the initial path away from S

n_steps = 0
current_node = [None, None] #row, column
direction = None

#find S
for i, d in enumerate(data):
	if 'S' in d:
		current_node = [i, d.find('S')]

#get next step in the loop
#has to be next to S:
#    | on top or bottom,
#    - on left or right, 
#    L on bottom or left,
#    J on bottom or right, 
#    F on top or left, 
#    7 on top or right
#just make a big switch case I guess 
if current_node[0] > 0 and data[current_node[0]][current_node[1]] == 'S': #check for OOB and that we haven't already adjusted this
	top = data[current_node[0]-1][current_node[1]]
	if top == '|' or top == 'F' or top == '7':
		current_node = [current_node[0]-1, current_node[1]]
		direction = 'up'

if current_node[0] < len(data) and data[current_node[0]][current_node[1]] == 'S':
	bottom = data[current_node[0]+1][current_node[1]]
	if bottom == '|' or bottom == 'J' or bottom == 'L':
		current_node = [current_node[0]+1, current_node[1]]
		direction = 'down'

if current_node[1] > 0 and data[current_node[0]][current_node[1]] == 'S':
	left = data[current_node[0]][current_node[1]-1]
	if left == '-' or left == 'L' or left == 'F':
		current_node = [current_node[0], current_node[1]-1]
		direction = 'left'

if current_node[1] < len(data[0]) and data[current_node[0]][current_node[1]] == 'S':
	right = data[current_node[0]][current_node[1]+1]
	if right == '-' or right == '7' or right == 'J':
		current_node = [current_node[0], current_node[1]+1]
		direction = 'right'
n_steps += 1

#now follow the pipes until you are back at S
#just make a big switch case again I guess 
pipe = data[current_node[0]][current_node[1]]
while pipe != 'S':
	n_steps += 1
	if direction == 'up':
		if pipe == '|':
			current_node = [current_node[0]-1,current_node[1]]
			direction = 'up' #unecessary but here for symmetry
		elif pipe == '7':
			current_node = [current_node[0],current_node[1]-1]
			direction = 'left' 
		elif pipe == 'F':
			current_node = [current_node[0],current_node[1]+1]
			direction = 'right' 
	elif direction == 'down':
		if pipe == '|':
			current_node = [current_node[0]+1,current_node[1]]
			direction = 'down' #unecessary but here for symmetry
		elif pipe == 'J':
			current_node = [current_node[0],current_node[1]-1]
			direction = 'left' 
		elif pipe == 'L':
			current_node = [current_node[0],current_node[1]+1]
			direction = 'right' 
	elif direction == 'right':
		if pipe == '-':
			current_node = [current_node[0],current_node[1]+1]
			direction = 'right' #unecessary but here for symmetry
		elif pipe == 'J':
			current_node = [current_node[0]-1,current_node[1]]
			direction = 'up' 
		elif pipe == '7':
			current_node = [current_node[0]+1,current_node[1]]
			direction = 'down'
	elif direction == 'left':
		if pipe == '-':
			current_node = [current_node[0],current_node[1]-1]
			direction = 'left' #unecessary but here for symmetry
		elif pipe == 'L':
			current_node = [current_node[0]-1,current_node[1]]
			direction = 'up' 
		elif pipe == 'F':
			current_node = [current_node[0]+1,current_node[1]]
			direction = 'down' 
	pipe = data[current_node[0]][current_node[1]]

print(f'Furthest distance from S: {n_steps // 2}')

#part 2

#have to do the same as part 1, except we have to track a grid to record interior and loop points,
# and also have to keep track of the orientation of the interior of the loop

current_node = [None, None] #row, column
direction = None

#build the grid that we will use to track interior points
grid = []
for i, d in enumerate(data):
	grid.append(list())
	for j in d:
		grid[i].append('0')

#find S
for i, d in enumerate(data):
	if 'S' in d:
		current_node = [i, d.find('S')]
grid[current_node[0]][current_node[1]] = '1' #update location of pipe on grid

#get next step in the loop
#has to be next to S:
#    | on top or bottom,
#    - on left or right, 
#    L on bottom or left,
#    J on bottom or right, 
#    F on top or left, 
#    7 on top or right
#just make a big switch case I guess 
if current_node[0] > 0 and data[current_node[0]][current_node[1]] == 'S': #check for OOB and that we haven't already adjusted this
	top = data[current_node[0]-1][current_node[1]]
	if top == '|' or top == 'F' or top == '7':
		current_node = [current_node[0]-1, current_node[1]]
		direction = 'up'

if current_node[0] < len(data) and data[current_node[0]][current_node[1]] == 'S':
	bottom = data[current_node[0]+1][current_node[1]]
	if bottom == '|' or bottom == 'J' or bottom == 'L':
		current_node = [current_node[0]+1, current_node[1]]
		direction = 'down'

if current_node[1] > 0 and data[current_node[0]][current_node[1]] == 'S':
	left = data[current_node[0]][current_node[1]-1]
	if left == '-' or left == 'L' or left == 'F':
		current_node = [current_node[0], current_node[1]-1]
		direction = 'left'

if current_node[1] < len(data[0]) and data[current_node[0]][current_node[1]] == 'S':
	right = data[current_node[0]][current_node[1]+1]
	if right == '-' or right == '7' or right == 'J':
		current_node = [current_node[0], current_node[1]+1]
		direction = 'right'

#set the grid points on the loop = 1
# set points to the right (left) of current direction = 'R' ('L')
# except 1 overrides 'L' and 'R'
def gr(node,ch): #this is potentially silly but whatever
	if node[0] > 0 and node[0] < len(data) and node[1] > 0 and node[1] < len(data[0]): #boundary conditions
		if grid[node[0]][node[1]] == '0':
			grid[node[0]][node[1]] = ch

#now follow the pipes until you are back at S
#just make a big switch case again I guess 
# running grid_replace on the straightaways
# then we'll deal with the grid afterwards
pipe = data[current_node[0]][current_node[1]]
while pipe != 'S':
	#grid[current_node[0]][current_node[1]] = data[current_node[0]][current_node[1]] #update location of pipe on grid
	grid[current_node[0]][current_node[1]] = '1' #update location of pipe on grid
	if direction == 'up':
		if pipe == '|':
			gr([current_node[0], current_node[1]+1], 'R')
			gr([current_node[0], current_node[1]-1], 'L')
			current_node = [current_node[0]-1,current_node[1]]
			direction = 'up' #unecessary but here for symmetry
		elif pipe == '7':
			gr([current_node[0]-1,current_node[1]], 'R')
			gr([current_node[0],current_node[1]+1], 'R')
			current_node = [current_node[0],current_node[1]-1]
			direction = 'left' 
		elif pipe == 'F':
			gr([current_node[0]-1,current_node[1]], 'L')
			gr([current_node[0],current_node[1]-1], 'L')
			current_node = [current_node[0],current_node[1]+1]
			direction = 'right' 
	elif direction == 'down':
		if pipe == '|':
			gr([current_node[0], current_node[1]+1], 'L')
			gr([current_node[0], current_node[1]-1], 'R')
			current_node = [current_node[0]+1,current_node[1]]
			direction = 'down' #unecessary but here for symmetry
		elif pipe == 'J':
			gr([current_node[0]+1,current_node[1]], 'L')
			gr([current_node[0],current_node[1]+1], 'L')
			current_node = [current_node[0],current_node[1]-1]
			direction = 'left' 
		elif pipe == 'L':
			gr([current_node[0]+1,current_node[1]], 'R')
			gr([current_node[0],current_node[1]-1], 'R')
			current_node = [current_node[0],current_node[1]+1]
			direction = 'right' 
	elif direction == 'right':
		if pipe == '-':
			gr([current_node[0]+1, current_node[1]], 'R')
			gr([current_node[0]-1, current_node[1]], 'L')
			current_node = [current_node[0],current_node[1]+1]
			direction = 'right' #unecessary but here for symmetry
		elif pipe == 'J':
			gr([current_node[0]+1,current_node[1]], 'R')
			gr([current_node[0],current_node[1]+1], 'R')
			current_node = [current_node[0]-1,current_node[1]]
			direction = 'up' 
		elif pipe == '7':
			gr([current_node[0]-1,current_node[1]], 'L')
			gr([current_node[0],current_node[1]+1], 'L')
			current_node = [current_node[0]+1,current_node[1]]
			direction = 'down'
	elif direction == 'left':
		if pipe == '-':
			gr([current_node[0]+1, current_node[1]], 'L')
			gr([current_node[0]-1, current_node[1]], 'R')
			current_node = [current_node[0],current_node[1]-1]
			direction = 'left' #unecessary but here for symmetry
		elif pipe == 'L':
			gr([current_node[0]+1,current_node[1]], 'L')
			gr([current_node[0],current_node[1]-1], 'L')
			current_node = [current_node[0]-1,current_node[1]]
			direction = 'up' 
		elif pipe == 'F':
			gr([current_node[0]-1,current_node[1]], 'R')
			gr([current_node[0],current_node[1]-1], 'R')
			current_node = [current_node[0]+1,current_node[1]]
			direction = 'down' 
	pipe = data[current_node[0]][current_node[1]]

#now we have to deal with the grid
#first we need to determine whether to use 'L' or 'R' (determine orientation of the loop)
# if we can find a connection between the edge of the grid and an 'L' or 'R' then we know that one cannot be enclosed
#returns the symbol of the exterior point
def find_LR(): #this has to be horrendously inefficient
	#start at top left corner, try to find an 'L' or 'R' with A*
	#unless top left corner is in the loop, you are guaranteed to find one of the two
	cn = [0, 0]
	if grid[cn[0]][cn[1]] == '1':
		print('top left corner is in the loop')
		exit()
	if grid[cn[0]][cn[1]] == 'R' or grid[cn[0]][cn[1]] == 'L':
		return grid[cn[0]][cn[1]]
	else:
		checked_nodes = set()
		to_check_nodes = [cn]
		while len(to_check_nodes) > 0:
			#check this node
			cn = to_check_nodes[0]
			if grid[cn[0]][cn[1]] == 'R' or grid[cn[0]][cn[1]] == 'L':
				return grid[cn[0]][cn[1]]
			#add all surrounding nodes that are not in checked_nodes to to_check_nodes	
			else:
				checked_nodes.add(tuple(cn))
				to_check_nodes = to_check_nodes[1:]
				if cn[0] > 0: #top
					if not(tuple([cn[0]-1,cn[1]]) in checked_nodes) and not([cn[0]-1,cn[1]] in to_check_nodes):
						if grid[cn[0]-1][cn[1]] != '1':
							to_check_nodes.append([cn[0]-1,cn[1]])
				if cn[0] < len(grid): #bottom
					if not(tuple([cn[0]+1,cn[1]]) in checked_nodes) and not([cn[0]+1,cn[1]] in to_check_nodes):
						if grid[cn[0]+1][cn[1]] != '1':
							to_check_nodes.append([cn[0]+1,cn[1]])
				if cn[1] > 0: #left
					if not(tuple([cn[0],cn[1]-1]) in checked_nodes) and not([cn[0],cn[1]-1] in to_check_nodes):
						if grid[cn[0]][cn[1]-1] != '1':
							to_check_nodes.append([cn[0],cn[1]-1])
				if cn[1] < len(grid[0]): #right
					if not(tuple([cn[0],cn[1]+1]) in checked_nodes) and not([cn[0],cn[1]+1] in to_check_nodes):
						if grid[cn[0]][cn[1]+1] != '1':
							to_check_nodes.append([cn[0],cn[1]+1])

#get the character that is actually interior to the loop
exterior_ch = find_LR()
if exterior_ch == 'R':
	interior_ch = 'L'
else:
	interior_ch = 'R'

#get all locations of interior_ch in the grids
to_fill = []
for i in range(len(grid)):
	for j in range(len(grid[i])):
		if grid[i][j] == interior_ch:
			to_fill.append([i,j])

#flood fill each enclosed point so that we get all the enclosed points
# making sure that if we locate another interior_ch in the process, we take that off the to_fill list
def flood_fill(loc):
	cn = loc
	checked_nodes = set()
	to_check_nodes = [cn]
	while len(to_check_nodes) > 0:
		grid[cn[0]][cn[1]] = interior_ch
		cn = to_check_nodes[0]
		checked_nodes.add(tuple(cn))
		try:
			to_fill.remove(cn) #don't flood fill points that don't need to be flood filled
		except ValueError:
			pass
		to_check_nodes = to_check_nodes[1:]
		if cn[0] > 0: #top
			if not(tuple([cn[0]-1,cn[1]]) in checked_nodes) and not([cn[0]-1,cn[1]] in to_check_nodes):
				if grid[cn[0]-1][cn[1]] != '1':
					to_check_nodes.append([cn[0]-1,cn[1]])
		if cn[0] < len(grid): #bottom
			if not(tuple([cn[0]+1,cn[1]]) in checked_nodes) and not([cn[0]+1,cn[1]] in to_check_nodes):
				if grid[cn[0]+1][cn[1]] != '1':
					to_check_nodes.append([cn[0]+1,cn[1]])
		if cn[1] > 0: #left
			if not(tuple([cn[0],cn[1]-1]) in checked_nodes) and not([cn[0],cn[1]-1] in to_check_nodes):
				if grid[cn[0]][cn[1]-1] != '1':
					to_check_nodes.append([cn[0],cn[1]-1])
		if cn[1] < len(grid[0]): #right
			if not(tuple([cn[0],cn[1]+1]) in checked_nodes) and not([cn[0],cn[1]+1] in to_check_nodes):
				if grid[cn[0]][cn[1]+1] != '1':
					to_check_nodes.append([cn[0],cn[1]+1])

while len(to_fill) > 0:
	flood_fill(to_fill[0])

#then count total number of enclosed points in the grid
n_interior = 0
for i in range(len(grid)):
	for j in range(len(grid[i])):
		if grid[i][j] == interior_ch:
			n_interior += 1

print(f'number of points interior to the loop: {n_interior}')