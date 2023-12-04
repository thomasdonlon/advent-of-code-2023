with open('day4input.txt', 'r') as f:
	data = f.readlines()

#part 1

n_wins = [] #storing n_wins means we only have to go through everything once
for line in data:
	line = line.split(':')[1] #remove Card X: Prefix
	line = line.split('|')
	winning_numbers = set(line[0].split())
	card_numbers = set(line[1].split())
	n_wins.append(len(winning_numbers.intersection(card_numbers)))

#2^(n-1) formula doesn't hold for n_win = 0 so we have to add the ternary
print(f'total points of all cards: {sum([(2**(n-1) if n > 0 else 0) for n in n_wins])}') 

#part 2

copies = dict()

#add one for the original card
for i in range(len(n_wins)):
	copies[i] = 1

#then add additional cards based on number of wins
for i, n in enumerate(n_wins):
	for j in range(n):
		copies[i+j+1] += copies[i]

#then total up number of cards
print(f'total number of cards: {sum(copies.values())}')