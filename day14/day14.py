with open('day14input.txt', 'r') as f:
	data = f.readlines()

#part 1

#copied/slightly adjusted from day 13 (was going to import but I'd have to do namespace main stuff)
def transpose(pattern): 
	out = []
	for i in range(len(pattern[0])):
		out.append('')
	for i, pvec in enumerate(pattern):
		for j, p in enumerate(pvec.strip()):
			out[j] += p
	return out 

#shift all round rocks as far upwards as they will go 
def roll_col(col):
	new_col = ''
	for i, c in enumerate(col):
		if c != 'O': #is stationary
			new_col += c
		else: #is a rolling rock
			#check how far up the rock can roll
			j = i
			while j > 0 and new_col[j-1] == '.':
				j -= 1
			if j == i: #could not roll the rock
				new_col += 'O'
			else: #rock rolled
				new_col = new_col[:j] + 'O' + new_col[j+1:] #some silly stuff bc strings are immutable
				new_col += '.' #replace the rock that rolled with an empty space
	return new_col 

#1 load at end of column, 2 at next step, etc.
def calc_load(col):
	load = 0
	col = col[::-1] #reverse the string
	for i, c in enumerate(col):
		if c == 'O':
			load += i + 1
	return load

#transpose data into columns, since rocks only roll inside a single column
columns = transpose(data)[:-1] #it has an extra line for some reason

# #testing
# rolled_cols = []
# for c in columns:
# 	rolled_cols.append(roll_col(c))
# for c in transpose(rolled_cols):
# 	print(c)

#shift all round rocks as far upwards as they will go 
#then calculate load
load = 0
for c in columns:
	load += calc_load(roll_col(c))

print(f'Total load: {load}')

#part 2

#I'm going to try to see if we reach a steady state at some point
#okay so the test reached a steady state with 7 cycles, let's see if we can identify one in the big dataset

#instead of transpose, we need a rotate function
def rotate(columns): 
	out = []
	for i in range(len(columns)):
		out.append('')
		for j in range(len(columns)): #it's square
			out[i] += columns[j][len(columns)-i-1]
	return out

#use this to determine how large the cycle is and where it starts
n_cycles = 1 #SET TO 200 OR SO
load_list = []
for cyc in range(n_cycles):
	for i in range(4):
		columns = [roll_col(c) for c in columns]
		columns = rotate(columns)
	load = 0
	for c in columns:
		load += calc_load(c)
	#print(cyc, load)
	if load in load_list:
		#print('previous index: ', load_list.index(load))
		pass
	load_list.append(load)

#in big data, 149 -> 115, (115 is start of steady state cycle)
#             150 -> 116,
#             151 -> 117, etc.
# so it is a 149-115 = 34 cycle steady state
# and 183 = 149 + 34 -> 115 too, so it works
# formula is ((N - 1 - 115)%34) + 115 is index of load (the extra -1 is because 149 is really cycle 150, since we started at 0)
# 1 billion -> 125, which has load = 85175

print('THIS PUZZLE WAS DONE WITH MANUAL INPUT; IT IS DOCUMENTED IN THE CODE, AND THE ANSWER FOR MY INPUT WAS 85175')