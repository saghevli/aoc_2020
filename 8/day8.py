import sys, string, re

def testProg(ins, returnAccWhenLoops):
  done = set()
  acc, i = 0, 0
  while i not in done and i < len(ins):
    done.add(i)
    if ins[i][0] == "acc":
      acc += ins[i][1]
    elif ins[i][0] == "jmp":
      i += ins[i][1]
      continue
    i += 1
  if i == len(ins) or returnAccWhenLoops:
    return acc
  return None

def testAllProgs(ins):
  for i in range(len(ins)):
    newIns = ins.copy()
    if ins[i][0] == "acc":
      continue
    if ins[i][0] == "jmp":
      newIns[i] = ("nop", ins[i][1])
    elif ins[i][0] == "nop":
      newIns[i] = ("jmp", ins[i][1])
    acc = testProg(newIns, False)
    if acc != None:
      return acc

ins = [(l.split()[0], int(l.split()[1])) for l in open(sys.argv[1]).read().split("\n")]
print('Part 1: ' + str(testProg(ins, True)))
print('Part 2: ' + str(testAllProgs(ins)))

