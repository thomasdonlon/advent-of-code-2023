with open('day2input.txt', 'r') as f:
	data = f.readlines()

#part 1
cum_sum = 0
for i, line in enumerate(data): #i+1 is game id
	rounds = line.strip().split(':')[1].split(';')
	
	#tally up # of cubes required for each round, tracking the max 
	r, g, b = 0, 0, 0 
	for rnd in rounds:
		rnd = rnd.split(',')
		for rndi in rnd:
			rndi = rndi.split()
			if rndi[-1] == 'red':
				r = max(int(rndi[0]), r)
			elif rndi[-1] == 'green':
				g = max(int(rndi[0]), g)
			elif rndi[-1] == 'blue':
				b = max(int(rndi[0]), b)

	#check that it fits the criteria
	if (r <= 12) and (g <= 13) and (b <= 14):
		cum_sum += (i+1)

print(f'sum of valid game ids: {cum_sum}')

#part 2
cum_sum = 0
for line in data:
	rounds = line.strip().split(':')[1].split(';')
	
	#tally up # of cubes required for each round, tracking the max 
	r, g, b = 0, 0, 0 
	for rnd in rounds:
		rnd = rnd.split(',')
		for rndi in rnd:
			rndi = rndi.split()
			if rndi[-1] == 'red':
				r = max(int(rndi[0]), r)
			elif rndi[-1] == 'green':
				g = max(int(rndi[0]), g)
			elif rndi[-1] == 'blue':
				b = max(int(rndi[0]), b)

	pwr = r*g*b
	cum_sum += pwr

print(f'sum of game powers: {cum_sum}')