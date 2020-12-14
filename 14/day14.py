import sys, re, collections
from copy import deepcopy


def part1(data):
  memory   = {}
  and_mask = 0
  or_mask  = 0
  for d in data:
      s   = d.split()
      key = s[0][0:3]
      if key == 'mem':
          addr  = int(s[0][4:-1])
          value = int(s[2])
          memory[addr] = (value & ~and_mask) | or_mask
          print("rightval: " + str((value & ~and_mask) | or_mask))
          print(value)
      if key == 'mas':
          and_mask = int(deepcopy(s[2]).replace('1', 'X').replace('0', '1').replace('X', '0'), 2)
          or_mask  = int(deepcopy(s[2]).replace('X', '0'), 2)
          print("r" + deepcopy(s[2]).replace('1', 'X').replace('0', '1').replace('X', '0'))
          print("r" + deepcopy(s[2]).replace('X', '0'))
  return sum([memory[x] for x in memory])


maskstr = ""
mem = collections.defaultdict(lambda : 0)
mask, zeromask = 0, 0 
for i, l in enumerate(open(sys.argv[1]).read().split("\n")):
  if l.startswith('mask'):
    r = re.match(r"mask = ([0-9A-Z]+)$", l)
    maskstr = r.group(1)
    zeromask = int(deepcopy(maskstr).replace('1', 'X').replace('0', '1').replace('X', '0'))
    # zeromask = int(deepcopy(maskstr).replace('1', '0').replace('X', '1'))
    mask = int(deepcopy(maskstr).replace('X', '0'), 2)
    print("w" +deepcopy(maskstr).replace('1', 'X').replace('0', '1').replace('X', '0'))
    # print("w" +deepcopy(maskstr).replace('1', '0').replace('X', '1'))
    print("w" +deepcopy(maskstr).replace('X', '0'))
  else:
    r = re.match(r"mem\[([0-9]+)\] = ([0-9]+)", l)
    w = (int(r.group(1)), int(r.group(2)))
    # print(w[1] & zeromask | mask)
    mem[w[0]] = (w[1] & ~zeromask) | mask
    print("wrongval: " + str((w[1] & ~zeromask) | mask))
    print(w[1])

# print(mem)
print(sum(v for v in mem.values()))
print(part1(open(sys.argv[1]).read().split("\n")))