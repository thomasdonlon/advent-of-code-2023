with open('day3input.txt', 'r') as f:
	data = f.readlines()

#remove all the newlines
for i, d in enumerate(data):
	data[i] = d.strip()

symbols = '%*/=#$@+&-'

#---------------------------------------
# part 1
#---------------------------------------

#get the starting and ending indices of the leftmost number in a string
def get_startend(s):
	trim = s.lstrip('.' + symbols)
	if len(trim) == 0: #no number in string, this is our end case
		return -1, -1

	start = len(s) - len(trim)

	#wish you could use find('.') for this but you have to account for symbols
	i = start
	while i < len(s) and s[i].isnumeric(): #can't go past edge of string
		i += 1
	end = i

	return start, end

#return tuples with (start, end) of all numbers in string
def get_all_startends(s):
	startend_list = []
	run_str = s
	run_end = 0 #used to track relative to whole string vs substring
	while 1:
		start, end = get_startend(run_str)
		if start == -1:
			return startend_list #sorry I usually hate defining functions this way without a return at the end
		startend_list.append((start+run_end, end+run_end))
		run_str = run_str[end:]
		run_end += end

#so I spent some time looking at the input and I don't think any numbers will ever be next to each other
#i.e. if there is anything next to a number, it must be a symbol
#if this proves to be wrong I will just have to redo this part

#is there any non-'.' characters next to a number?
#number is determined from its start and end values, and the row it's in
def is_machine_part(row, start, end):

	#make sure we don't go out of bounds
	adj_start = max(start-1,0)
	adj_end = min(end+1,len(data[row])-1)
	
	if row > 0: #check row above
		test = data[row-1][adj_start:adj_end]
		if len(test.lstrip('.')) > 0: #then there must be a character here
			return True
	if row < len(data) - 1: #check row below
		test = data[row+1][adj_start:adj_end]
		if len(test.lstrip('.')) > 0:
			return True

	#check in row
	if start > 0:
		if data[row][start-1] != '.':
			return True
	if end < len(data[row]) - 1:
		if data[row][end] != '.':
			return True

	return False

#runtime
cum_sum = 0
for row, line in enumerate(data):
	startends = get_all_startends(line)
	for se in startends:
		start, end = se[0], se[1]
		if is_machine_part(row, start, end):
			cum_sum += int(line[start:end])

print(f'Sum of all machine part numbers: {cum_sum}')

#---------------------------------------
# part 2
#---------------------------------------

#get adjacent numbers to the point (row, col)
def get_adjacent_numbers(all_nums, row, col):
	#this could probably be shortened in some way but this is fine

	adj_nums = []

	if row > 0: #check row above
		for se in all_nums[row-1]:
			start, end = se[0], se[1]
			if col >= start-1 and col < end+1:
				adj_nums.append(int(data[row-1][start:end]))

	if row < len(all_nums) - 1: #check row below
		for se in all_nums[row+1]:
			start, end = se[0], se[1]
			if col >= start-1 and col < end+1:
				adj_nums.append(int(data[row+1][start:end]))

	#check current row
	for se in all_nums[row]:
		start, end = se[0], se[1]
		if col >= start-1 and col < end+1:
			adj_nums.append(int(data[row][start:end]))

	return adj_nums

#runtime
cum_sum = 0

#collect the locations of all numbers in the data
all_nums = []
for row, line in enumerate(data):
	startends = get_all_startends(line)
	all_nums.append(startends)

#get positions of every * in the data
gear_positions = []
for row, line in enumerate(data):
	for i, ch in enumerate(line):
		if ch == '*':
			gear_positions.append((row, i))

for pos in gear_positions:
	adj_nums = get_adjacent_numbers(all_nums, pos[0], pos[1])
	if len(adj_nums) == 2:
		gear_ratio = adj_nums[0] * adj_nums[1]
		cum_sum += gear_ratio

print(f'Sum of all gear ratios: {cum_sum}')