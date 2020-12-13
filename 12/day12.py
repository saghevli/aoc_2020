import sys, collections, copy

dirs = {'E': (0, -1), 'S': (1, 0), 'W': (0, 1), 'N': (-1, 0)}
dirNames = ["E", "S", "W", "N"]

def part1(instructions):
  dir = "E"
  i, j = 0, 0
  for ins in instructions:
    # print(ins)
    if ins[0] == "F":
      i += ins[1]*dirs.get(dir)[0]
      j += ins[1]*dirs.get(dir)[1]
    elif ins[0] == "L":
      dir = dirNames[(dirNames.index(dir) - int(ins[1]/90)) % 4]
    elif ins[0] == "R":
      dir = dirNames[(dirNames.index(dir) + int(ins[1]/90)) % 4]
    else:
      i += ins[1]*dirs.get(ins[0])[0]
      j += ins[1]*dirs.get(ins[0])[1]
  return (i, j)

def part2(instructions):
  i, j, wi, wj = 0, 0, -1, 10
  for ins in instructions:
    print(ins)
    di = wi-i
    dj = wj-j
    print("dj: " + str(dj) + " di: " + str(di))
    if ins[0] in ["N", "S", "E", "W"]:
      wi += ins[1]*dirs.get(ins[0])[0]
      wj += ins[1]*dirs.get(ins[0])[1]
    elif ins[0] == "F":
      i += (di)*ins[1]
      j += (dj)*ins[1]
      wi += (di)*ins[1]
      wj += (dj)*ins[1]
    else:
      if ins[1] == 180:
        wi += -2*di
        wj += -2*dj
      elif (ins[0] == "L" and ins[1] == 90) or\
        (ins[0] == "R" and ins[1] == 270):
        tmp = di
        di = -dj
        dj = tmp
        print("rotated dj: " + str(dj) + " di: " + str(di))
        wi = i + di
        wj = j + dj
        print("new wj: " + str(wj) + " wi: " + str(wi))
      elif (ins[0] == "R" and ins[1] == 90) or\
        (ins[0] == "L" and ins[1] == 270):
          tmp = dj
          dj = -di
          di = tmp
          print("rotated dj: " + str(dj) + " di: " + str(di))
          wi = i + di
          wj = j + dj
          print("new wj: " + str(wj) + " wi: " + str(wi))
      else:
        print("should never happen")
    print("ship: " + str(j) + ", " + str(i) +\
      " way: " + str(wj) + ", " + str(wi))
  return (i, j)

instructions = [(l[0], int(l[1:])) for l in open(sys.argv[1]).read().split("\n")]
point = part1(instructions)
point2 = part2(instructions)
print(abs(point[0]) + abs(point[1]))
print(abs(point2[0]) + abs(point2[1]))