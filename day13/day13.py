with open('day13input.txt', 'r') as f:
	data = f.readlines()

#split the data into the individual patterns
patterns = []
pattern = []
for line in data:
	line = line.strip()
	if line == '':
		patterns.append(pattern)
		pattern = []
	else:
		pattern.append(line)
patterns.append(pattern) #get last pattern

# part 1

def transpose(pattern):
	out = []
	for i in range(len(pattern[0])):
		out.append('')
	for i, pvec in enumerate(pattern):
		for j, p in enumerate(pvec):
			out[j] += p
	return out

def find_horizontal_lor(pattern):

	def is_mirrored(pattern, i):
		top = pattern[:i]
		bottom = pattern[i:]

		if len(top) > 0 and len(bottom) > 0:
			#make them the same length, cut first n rows off of top and bottom n rows off of bottom to make lengths match
			diff = len(top) - len(bottom)
			if diff > 0: #top is longer
				top = top[diff:]
			elif diff < 0:
				bottom = bottom[:diff]

			top.reverse()
			for t, b in zip(top, bottom):
				if t != b:
					return False
			return True
		return False #edge case if top is empty (i = 0) or no match was found

	for i in range(len(pattern)):
		if is_mirrored(pattern, i):
			return i

	return None #no match was found

def find_vertical_lor(pattern):
	pattern = transpose(pattern)
	return find_horizontal_lor(pattern)

cum_sum = 0
for pattern in patterns:

	#check for horizontal reflection
	hsplit = find_horizontal_lor(pattern)
	if hsplit is not None:
		cum_sum += 100*hsplit
	else: #check for vertical reflection
		vsplit = find_vertical_lor(pattern)
		cum_sum += vsplit

print(f'Output number: {cum_sum}')

# part 2

#count differences instead of evaluating symmetry
#if only 1 difference, that is the new reflection point

def find_new_horizontal_lor(pattern):

	def count_differences(pattern, i):
		tot_diffs = 0

		top = pattern[:i]
		bottom = pattern[i:]

		if len(top) > 0 and len(bottom) > 0:
			#make them the same length, cut first n rows off of top and bottom n rows off of bottom to make lengths match
			diff = len(top) - len(bottom)
			if diff > 0: #top is longer
				top = top[diff:]
			elif diff < 0:
				bottom = bottom[:diff]

			top.reverse()
			for t, b in zip(top, bottom):
				for ti, bi in zip(t, b):
					if ti != bi:
						tot_diffs += 1
		return tot_diffs 

	for i in range(len(pattern)):
		if count_differences(pattern, i) == 1:
			return i

	return None #no match was found

def find_new_vertical_lor(pattern):
	pattern = transpose(pattern)
	return find_new_horizontal_lor(pattern)

cum_sum = 0
for pattern in patterns:

	#check for horizontal reflection
	hsplit = find_new_horizontal_lor(pattern)
	if hsplit is not None:
		cum_sum += 100*hsplit
	else: #check for vertical reflection
		vsplit = find_new_vertical_lor(pattern)
		cum_sum += vsplit

print(f'Output number: {cum_sum}')