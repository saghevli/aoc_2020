import sys
data = open(sys.argv[1]).read().splitlines()
ids = [sum([(c in 'BR')*(2**(9-e)) for (c,e) in zip(s,range(10))]) for s in data]
for val in range(min(ids),max(ids)+1):
	if val not in ids: print('Part two: '+str(val))
print('Part one: '+str(val))