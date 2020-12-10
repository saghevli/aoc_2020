import sys, collections

nums = sorted([int(l) for l in open(sys.argv[1]).read().split("\n")])
combs = collections.defaultdict(int, {0: 1})
for num in nums:
  combs[num] = combs[num - 1]\
    + combs[num - 2]\
    + combs[num - 3]
print(combs[nums[-1]])
