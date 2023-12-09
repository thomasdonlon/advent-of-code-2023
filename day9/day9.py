with open('day9input.txt', 'r') as f:
	data = f.readlines()

#part 1

def predict_next_val(vals): #recursive
	if sum([v**2 for v in vals]) == 0: #if sum of squares is 0, they are all 0
		return 0
	else:
		dvals = [vals[i+1] - vals[i] for i in range(len(vals)-1)] #get differences
		dvals.append(predict_next_val(dvals)) #add next term
		return vals[-1] + dvals[-1]

cum_sum = 0
for line in data:
	vals = [int(i) for i in line.strip().split()]
	cum_sum += predict_next_val(vals)

print(f'total sum of all predictions: {cum_sum}')

#part 2

def predict_prev_val(vals): #recursive
	if sum([v**2 for v in vals]) == 0: #if sum of squares is 0, they are all 0
		return 0
	else:
		dvals = [vals[i+1] - vals[i] for i in range(len(vals)-1)] #get differences 
		dvals = [predict_prev_val(dvals)] + dvals #add prev term to beginning 
		return vals[0] - dvals[0]

cum_sum = 0
for line in data:
	vals = [int(i) for i in line.strip().split()]
	cum_sum += predict_prev_val(vals)

print(f'total sum of all predictions: {cum_sum}')