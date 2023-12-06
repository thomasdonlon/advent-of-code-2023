#unecessarily optimized the shit out of this to beat my friends who all think they're smart

#reading inputs is for chumps
race_times = [42, 89, 91, 89]
record_dists = [308, 1170, 1291, 1467]

#part 1

cum_prod = 1
for i, rt in enumerate(race_times):
	for t in range(rt):
		d = (rt - t)*t #get mathed
		if d > record_dists[i]:
			cum_prod *= (rt - 2*t + 1) #get mathed again
			break

print(f'Total number of ways to win all races: {cum_prod}')

# part 2

rt = 42899189
record_dist = 308117012911467

n_ways = (rt - 2*int(0.5*(rt - (rt**2 - 4*record_dist)**0.5)) -1) #get mathed yet again

print(f'Total number of ways to win the race: {n_ways}')
