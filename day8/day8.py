import re #I want to get better at regex

with open('day8input.txt', 'r') as f:
	data = f.readlines()

#part 1

#get RL list -> 0 (left) and 1 (right)
rl_instructions = []
for ch in data[0].strip():
	rl_instructions.append(int(ch == 'R'))
#print(rl_instructions)

nodes = dict()
for line in data[2:]: #build the node dictionary
	name, left, right = re.findall(r"\w+", line)
	nodes[name] = [left, right]

current_node = 'AAA'
current_instruction = 0
n_iter = 0
while current_node != 'ZZZ':
	if current_instruction == len(rl_instructions): #reset to beginning of instructions if they run out
		current_instruction = 0
	current_node = nodes[current_node][rl_instructions[current_instruction]]
	current_instruction += 1
	n_iter += 1

print(f'Steps to get to ZZZ: {n_iter}')

#part 2

distances = []
starting_nodes = [n for n in nodes.keys() if n[2] == 'A']

for sn in starting_nodes:
	current_node = sn
	current_instruction = 0
	n_iter = 0
	while current_node[2] != 'Z':
		if current_instruction == len(rl_instructions): #reset to beginning of instructions if they run out
			current_instruction = 0
		current_node = nodes[current_node][rl_instructions[current_instruction]]
		current_instruction += 1
		n_iter += 1
	distances.append(n_iter)

#shortest distance for all nodes to get to ..Z is the LCM of their individual distances
#total length is too large to compute by loop
def LCM(a, b):
	return int(a*b/GCD(a,b))

def GCD(a, b): #I hope I never have to do this again
	ri = 1
	rm2 = a % b
	if rm2 == 0:
		return min((a, b))
	rm1 = b % rm2
	if rm1 == 0:
		return rm2
	ri = rm2 % rm1
	while ri != 0:
		rm2 = rm1
		rm1 = ri
		ri = rm2 % rm1
	return rm1

out = distances[0]
for d in distances:
	out = LCM(out, d)

print(f'Steps to get to all ..Z nodes: {out}')