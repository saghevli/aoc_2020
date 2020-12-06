import sys
groups = open(sys.argv[1]).read().split("\n\n")
# Part one
print(sum(len(set.union(*map(set, g.split('\n')))) for g in groups))
# Part two
print(sum(len(set.intersection(*map(set, g.split('\n')))) for g in groups))