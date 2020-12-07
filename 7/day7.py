import sys, string, re
b = {}

def recurseColorGold(color):
  if (color == "shiny gold"):
    return True
  elif not b[color]:
    return False
  containsGold = False
  for value in b[color][0]:
    containsGold = containsGold | recurseColorGold(value)
  return containsGold

def recurseSumGold(color):
  if not b[color][0]:
    return 1
  return 1+sum(recurseSumGold(b[color][0][i])*int(b[color][1][i])
    for i in range(len(b[color][0])))

for l in open(sys.argv[1]).read().split("\n"):
  lA = l.split(" bags contain ")
  b[lA[0]] = (re.findall(r"[0-9]+ (.+?) bag[s,.]", lA[1]),
    re.findall(r"([0-9]+) .+? bag[s,.]", lA[1]))

print('Part one: '+ str(sum(recurseColorGold(key) for key in b)))
print('Part two: '+ str(recurseSumGold("shiny gold")))
