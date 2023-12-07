with open('day7input.txt', 'r') as f:
	data = f.readlines()

#part 1

#=========================================================
#class implementation 

def convert_to_aloi(astr):
	out = []
	for ch in astr:
		if ch == 'A': #none of this alphanumeric nonsense, we deal with ints in this house
			out.append(14)
		elif ch == 'K':
			out.append(13)
		elif ch == 'Q':
			out.append(12)
		elif ch == 'J':
			out.append(11)
		elif ch == 'T':
			out.append(10)
		else:
			out.append(int(ch))
	return out

def get_type(aloi):
	#convert to a dict with number of each card
	cards = {}
	for i in range(14): #build the dict so every number is 0
		cards[i+1] = 0 
	for i in aloi: #add the cards to the dict
		cards[i] += 1

	return sum([i**2 for i in cards.values()])

def tiebreaker(hand1, hand2):
	for h1, h2 in zip(hand1.cards, hand2.cards):
		if h1 < h2:
			return -1
		elif h1 > h2:
			return 1

class Hand:

	def __init__(self, astr):
		self.cards = convert_to_aloi(astr)
		self.type = get_type(self.cards) #25 for 5 of a kind, 17 for 4 of a kind, 13 for full house, ... 5 for high card,
										 # you can use the sum of the squares of # of each card to get a unique (ordered) solution

	def __lt__(self, other):
		if self.type == other.type:
			for h1, h2 in zip(self.cards, other.cards):
				if h1 < h2:
					return True
				elif h1 > h2:
					return False
		return (self.type < other.type)

#=========================================================

#runtime
hands = []
bids = []
for line in data:
	line = line.strip().split()
	hands.append(Hand(line[0]))
	bids.append(int(line[1]))

bids = [b for _,b in sorted(zip(hands, bids))]
hands.sort()

cum_sum = 0
for i, bid in enumerate(bids):
	cum_sum += (i+1)*bid

print(f'Sum of all winnings: {cum_sum}')



#part 2

#=========================================================
#class implementation 
#have to redefine a couple functions for new Joker functionality

def convert_to_aloi(astr):
	out = []
	for ch in astr:
		if ch == 'A': #none of this alphanumeric nonsense, we deal with ints in this house
			out.append(13)
		elif ch == 'K':
			out.append(12)
		elif ch == 'Q':
			out.append(11)
		elif ch == 'J':
			out.append(1)
		elif ch == 'T':
			out.append(10)
		else:
			out.append(int(ch))
	return out

def get_type(aloi):
	#convert to a dict with number of each card
	cards = {}
	for i in range(13): #build the dict so every number is 0
		cards[i+1] = 0 

	n_jokers = 0
	for i in aloi: #add the cards to the dict
		if i != 1:
			cards[i] += 1
		else:
			n_jokers += 1

	#jokers always want to be added to largest number
	for i in range(n_jokers):
		cards[list(cards.keys())[list(cards.values()).index(max(cards.values()))]] += 1 #this is a mess but hey it works

	return sum([i**2 for i in cards.values()])

# class Hand:

# 	def __init__(self, astr):
# 		self.cards = convert_to_aloi(astr)
# 		self.type = get_type(self.cards) #25 for 5 of a kind, 17 for 4 of a kind, 13 for full house, ... 5 for high card,
# 										 # you can use the sum of the squares of # of each card to get a unique (ordered) solution

# 	def __lt__(self, other):
# 		if self.type == other.type:
# 			for h1, h2 in zip(self.cards, other.cards):
# 				if h1 < h2:
# 					return True
# 				elif h1 > h2:
# 					return False
# 		return (self.type < other.type)

#=========================================================

#runtime
hands = []
bids = []
for line in data:
	line = line.strip().split()
	hands.append(Hand(line[0]))
	bids.append(int(line[1]))

bids = [b for _,b in sorted(zip(hands, bids))]
hands.sort()

cum_sum = 0
for i, bid in enumerate(bids):
	cum_sum += (i+1)*bid

print(f'Sum of all winnings: {cum_sum}')