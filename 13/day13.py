import sys, collections, copy

depart = 0
buslines = []
lines = [str(l) for l in open(sys.argv[1]).read().split("\n")]
for i in range(len(lines)):
  if i == 0:
    depart = int(lines[i])
  else:
    buslines = [int(id) for id in lines[i].split(",") if id is not "x"]
print(buslines)

i = depart
first = 0
while i > 0:
  for line in buslines:
    if i % line == 0:
      print(line*(i-depart))
      i = -1
      break
  i += 1

