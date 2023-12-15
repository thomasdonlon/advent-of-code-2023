with open('day15input.txt', 'r') as f:
	data = f.readlines()[0].split(',')

#part 1

def do_hash(astr):
	out = 0
	for ch in astr:
		if ch == '\n':
			pass
		else:
			out += ord(ch) #gets ascii code
			out *= 17
			out = out % 256
	return out

cum_sum = 0
for item in data:
	cum_sum += do_hash(item)

print(f'Sum of all hashes: {cum_sum}')

#part 2

def remove_lens(label, boxes, boxn):
	for i, lens in enumerate(boxes[boxn]): 
		if lens[0] == label:
			boxes[boxn].pop(i)

def add_swap_lens(label, lensn, boxes, boxn):
	replaced = False
	for i, lens in enumerate(boxes[boxn]):
		if lens[0] == label:
			boxes[boxn][i][1] = lensn
			replaced = True
	if not replaced:
		boxes[boxn].append([label, lensn])

#build boxes array
boxes = list()
for i in range(256):
	boxes.append(list())

#do all the lens swapping
for item in data:
	#check if '-' or '='
	item = item.replace('\n', '')
	if item[-1] == '-':
		boxn = do_hash(item[:-1])
		remove_lens(item[:-1], boxes, boxn)
	else: #is '='
		item = item.split('=')
		boxn = do_hash(item[0])
		add_swap_lens(item[0], int(item[1]), boxes, boxn)

#calculate focusing power
focusing_power = 0
for i, box in enumerate(boxes):
	for j, lens in enumerate(box):
		focusing_power += (i+1)*(j+1)*lens[1]

print(f'Focusing power: {focusing_power}')