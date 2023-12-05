with open('day5input.txt', 'r') as f:
	data = f.readlines()

# part 1

def convert(inputs, maps):
	#an element of maps is [dest_start, source_start, range]

	outputs = [None for i in inputs] #this tracks if we've mapped each number 

	for m in maps:
		dest_start = m[0] #just makes things more readable
		source_start = m[1]
		ran = m[2]

		for i, el in enumerate(inputs):
			if el >= source_start and el < source_start + ran:
				outputs[i] = dest_start + el - source_start

	#fix any values that were not mapped
	for i in range(len(outputs)):
		if outputs[i] is None:
			outputs[i] = inputs[i]

	return outputs

#runtime

#split the data into the individual sections
data_adj = [[],]
i = 0
for line in data:
	line = line.strip()
	if line == '':
		i += 1
		data_adj.append([])
	else:
		data_adj[i].append(line)

#get seed numbers 
seeds = [int(i) for i in data_adj[0][0].split(':')[1].split()]

#format rest of data and do the conversions
out = seeds.copy()
for section in data_adj[1:]: #don't get seed data again
	maps = []
	for i in section[1:]: #skip the name of the section
		maps.append([int(j) for j in i.split()])
	out = convert(out, maps)

print(f'Minimum location of seed: {min(out)}')

#part 2

def split_inputs(nums, ranges, maps):
	#an element of inputs is now [start, range]
	#an element of maps is [dest_start, source_start, range]

	split_nums = []
	split_ranges = []

	#collect locations of splits
	split_ids = [] #have to split on all source_starts and source_ends 
	for m in maps:
		source_start = m[1] #just makes things more readable
		ran = m[2]
		split_ids.append(source_start)
		split_ids.append(source_start + ran)

	#split all the inputs on split_ids
	for num, ran in zip(nums, ranges):
		si_between = []
		for si in split_ids: #collect all ids we need to split on for this given num and ran
			if si > num and si <= num + ran:
				si_between.append(si)
		si_between.sort()

		if len(si_between) == 0: #there's probably a more clever way to do this without if/else but I'm not seeing it quickly
			split_nums.append(num)
			split_ranges.append(ran)
		else:
			split_nums.append(num) #add the original num and adjusted ran

			last_num = num #have to track how much of the range has been used so far
			for si in si_between:

				split_nums.append(si)
				split_ranges.append(si - last_num)
				last_num = si

			split_ranges.append(num+ran-last_num) #this syncs everything up

	#remove 0 ranges
	#yes I know this is sloppy but I can't think of a better way to symmetrically remove items from 2 lists right now
	remove_inds = []
	for i in range(len(split_nums)):
		if split_ranges[i] == 0:
			remove_inds.append(i)

	remove_inds.reverse() #ensures you actually hit everything bc the list changes size
	for el in remove_inds:
		split_nums.pop(el)
		split_ranges.pop(el)

	return split_nums, split_ranges

#runtime

#get seed numbers 
seeds = [int(i) for i in data_adj[0][0].split(':')[1].split()]
seed_nums = [seeds[2*i] for i in range(len(seeds)//2)]
seed_ranges = [seeds[2*i+1] for i in range(len(seeds)//2)]

#format rest of data and do the conversions
out_nums, out_ranges = seed_nums.copy(), seed_ranges.copy()
for section in data_adj[1:]: #don't get seed data again
	maps = []
	for i in section[1:]: #skip the name of the section
		maps.append([int(j) for j in i.split()])
	print(out_nums, out_ranges, maps)
	out_nums, out_ranges = split_inputs(out_nums, out_ranges, maps) #make sure no ranges extend between ranges
	out_nums = convert(out_nums, maps) #now can just convert the nums
	print(out_nums, out_ranges)
	print()

print(f'Minimum location of seed: {min(out_nums)}')