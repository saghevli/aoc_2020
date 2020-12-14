import sys, re, collections, itertools
from copy import deepcopy

def f(p):
  if p[0] == '0':
    return p[1]
  if p[0] == '1':
    return '1'
  if p[0] == 'X':
    return 'X'


mem = collections.defaultdict(lambda : 0)
mask, zeromask = 0, 0 
for i, l in enumerate(open(sys.argv[1]).read().split("\n")):
  if l.startswith('mask'):
    r = re.match(r"mask = ([0-9A-Z]+)$", l)
    maskstr = r.group(1)
    zeromask = int(maskstr.replace('1', '0').replace('X', '1'), 2)
    mask = int(maskstr.replace('X', '0'), 2)
  else:
    r = re.match(r"mem\[([0-9]+)\] = ([0-9]+)", l)
    w = (int(r.group(1)), int(r.group(2)))
    mem[w[0]] = (w[1] & zeromask) | mask

print("part 1: " + str(sum(v for v in mem.values())))

mem = collections.defaultdict(lambda : 0)
zeromask = 0
mask = ""
for i, l in enumerate(open(sys.argv[1]).read().split("\n")):
  if l.startswith('mask'):
    r = re.match(r"mask = ([0-9A-Z]+)$", l)
    mask = r.group(1)
  else:
    r = re.match(r"mem\[([0-9]+)\] = ([0-9]+)", l)
    w = (int(r.group(1)), int(r.group(2)))
    masks = []
    for bs in list(itertools.product(range(2), repeat=mask.count('X'))):
      newmask = "".join(list(f(p) for p in zip(mask, format(w[0], "036b"))))
      for b in bs:
        newmask = newmask.replace('X', str(b), 1)
      masks.append(newmask)
    for m in masks:
      mem[m] = w[1]
print("part 2: " + str(sum(v for v in mem.values())))