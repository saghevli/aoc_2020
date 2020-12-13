import sys, collections, copy

def adjacentFilled(map, i, j):
  left, right, top, bottom = False, False, False, False
  if i == 0:
    top = True
  elif i == len(map)-1:
    bottom = True
  if j == 0:
    left = True
  elif j == len(map[0])-1:
    right = True

  toCheck = []
  if not top:
    toCheck.append((i-1, j))
    if not left:
      toCheck.append((i-1, j-1))
    if not right:
      toCheck.append((i-1, j+1))
  if not bottom:
    toCheck.append((i+1, j))
    if not left:
      toCheck.append((i+1, j-1))
    if not right:
      toCheck.append((i+1, j+1))
  if not left:
    toCheck.append((i, j-1))
  if not right:
    toCheck.append((i, j+1))
  
  count = 0
  for p in toCheck:
    if map[p[0]][p[1]] == "#":
      count+=1
  return count

def adjacentVisibile(map, i, j):
  deltas = [\
    (-1, -1), (-1, 0), (-1, +1),\
    (0, -1), (0, 1),\
    (1, -1), (1, 0), (1, 1),\
  ]
  occupiedDirections = 0
  for d in deltas:
    k, l = i, j
    k += d[0]
    l += d[1]
    while k >= 0 and k < len(map) and l >= 0 and l < len(map[0]):
      if map[k][l] == "#":
        occupiedDirections += 1
        break
      elif map[k][l] == "L":
        break
      k += d[0]
      l += d[1]
  return occupiedDirections


def movement(map, sightFn, threshold):
  delta = -1
  newMap = copy.deepcopy(map)
  while delta != 0:
    delta = 0
    for i in range(len(map)):
      for j in range(len(map[0])):
        if map[i][j] == '.':
          continue
        filled = sightFn(map, i, j)
        if map[i][j] == "#" and filled >= threshold:
          delta += 1
          newMap[i][j] = "L"
        elif map[i][j] == "L" and filled == 0:
          delta += 1
          newMap[i][j] = "#"
    map = copy.deepcopy(newMap)
  return map

map = [list(l) for l in open(sys.argv[1]).read().split("\n")]
print("part 1: " + str(sum(l.count("#") for l in
  movement(map, adjacentFilled, 4))))
print("part 2: " + str(sum(l.count("#") for l in
  movement(map, adjacentVisibile, 5))))
