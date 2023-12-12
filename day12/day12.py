with open('day12input.txt', 'r') as f:
	data = f.readlines()

#part 1

def is_allowed(springs, test_str):
	#? are wildcards, X and . must be the same
	for ch1, ch2 in zip(springs, test_str):
		if not((ch1 == ch2) or (ch1 == '?')):
			return False
	return True

def generate_possible(remaining_str, vals):
	all_values = []

	base_str = ''
	for i in range(vals[0]):
		base_str += '#'

	if len(vals) == 1: #this is last value
		diff = len(remaining_str) - len(base_str)
		while diff >= 0:
			tmp = base_str
			for i in range(diff):
				tmp += '.'
			if is_allowed(remaining_str, tmp):
				all_values.append(tmp)

			base_str = '.' + base_str
			diff -= 1
		
	else: #more values afterwards, recurse
		base_str += '.'

		diff = len(remaining_str) - len(base_str)
		#print(diff, vals[1:], sum(vals[1:]) + len(vals[1:]) - 1)
		while diff >= sum(vals[1:]) + len(vals[1:]) - 1: #minimum length of vals including 1 separating '.'
			if is_allowed(remaining_str, base_str):
				for pv in generate_possible(remaining_str[len(base_str):], vals[1:]):
					all_values.append(base_str + pv)
			base_str = '.' + base_str
			diff -= 1

	return all_values

def n_perms(springs, vals):
	#just brute force compare each line to all possibilities
	n_allowed = 0

	#generate all possible test strings with vals
	test_strings = generate_possible(springs, vals)
	#return len(test_strings)
	#print(test_strings)
	#print()

	#test all the possible test strings
	for test_str in test_strings:
		#print(springs, test_str)
		if is_allowed(springs, test_str):
			n_allowed += 1
			#print('true')

	return n_allowed

cum_sum = 0
for line in data:
	line = line.strip().split()
	cum_sum += n_perms(line[0], [int(i) for i in line[1].split(',')])

print(f'Sum of all possible combinations: {cum_sum}')

#part 2

known_dict = {}

def is_allowed(springs, test_str):
	#? are wildcards, X and . must be the same
	for ch1, ch2 in zip(springs, test_str):
		if not((ch1 == ch2) or (ch1 == '?')):
			return False
	return True

def generate_possible(remaining_str, vals):

	#check memoization
	if remaining_str + ' ' + str(vals) in known_dict.keys():
		return known_dict[remaining_str + ' ' + str(vals)]
	else:

		n_vals = 0

		base_str = ''
		for i in range(vals[0]):
			base_str += '#'

		if len(vals) == 1: #this is last value
			diff = len(remaining_str) - len(base_str)
			while diff >= 0:
				tmp = base_str
				for i in range(diff):
					tmp += '.'
				if is_allowed(remaining_str, tmp):
					n_vals += 1

				base_str = '.' + base_str
				diff -= 1
			
		else: #more values afterwards, recurse
			base_str += '.'

			diff = len(remaining_str) - len(base_str)
			#print(diff, vals[1:], sum(vals[1:]) + len(vals[1:]) - 1)
			while diff >= sum(vals[1:]) + len(vals[1:]) - 1: #minimum length of vals including 1 separating '.'
				if is_allowed(remaining_str, base_str):
					n_vals += generate_possible(remaining_str[len(base_str):], vals[1:])
				base_str = '.' + base_str
				diff -= 1

		known_dict[remaining_str + ' ' + str(vals)] = n_vals
		return n_vals

cum_sum = 0
for line in data:
	line = line.strip().split()
	l = [int(i) for i in line[1].split(',')]
	lout = []
	outstr = ''
	for i in range(5):
		lout += l.copy()
		outstr += line[0] + '?'
	outstr = outstr[:-1] #remove trailing '?'
	val = generate_possible(outstr, lout)
	cum_sum += val

print(f'Sum of all possible combinations: {cum_sum}')