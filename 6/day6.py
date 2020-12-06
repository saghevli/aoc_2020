import sys, string
part1, part2 = 0, 0
for g in open(sys.argv[1]).read().split("\n\n"):
  pS = g.split("\n")
  a = {}
  for p in pS:
    for q in p:
      if q not in a:
        a[q] = 0 
      a[q]+=1
  for x in string.ascii_lowercase:
    if x in a:
      part1+=1
      if a[x] == len(pS):
        part2+=1
print('Part one: '+str(part1))
print('Part two: '+str(part2))