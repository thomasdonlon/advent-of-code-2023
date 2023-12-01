with open('day1input.txt', 'r') as f:
	data = f.readlines()

#part 1
cal_sum = 0
for line in data:
	line = line.strip() #not necessary but helpful for printing

	#get first char
	val1 = None
	i = 0
	while val1 is None:
		if line[i].isnumeric():
			val1 = line[i]
		i += 1

	#get second char
	val2 = None
	i = 1
	while val2 is None:
		if line[-i].isnumeric():
			val2 = line[-i]
		i += 1

	cal_sum += int(val1+val2)

print(f'Part 1: sum of calibration values: {cal_sum}')

#part 2
valid_chars = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
cal_sum = 0
for line in data:
	line = line.strip() #not necessary but helpful for printing

	#format each string so that all the valid chars substrings are replaced with the corresponding numerical values
	for i, ch in enumerate(valid_chars):
		line = line.replace(ch, ch+str(i+1)+ch) #have to keep the text on either side bc of overlaps (e.g. eightwo)

	#get first char
	val1 = None
	i = 0
	while val1 is None:
		if line[i].isnumeric():
			val1 = line[i]
		i += 1

	#get second char
	val2 = None
	i = 1
	while val2 is None:
		if line[-i].isnumeric():
			val2 = line[-i]
		i += 1

	cal_sum += int(val1+val2)

print(f'Part 2: sum of calibration values: {cal_sum}')