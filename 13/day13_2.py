import sys, collections, copy, functools

def chinese_remainder(n, a):
    sum = 0
    prod = functools.reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

buslines = []
linearr = [str(l) for l in open(sys.argv[1]).read().split("\n")][1].split(",")
buslines = [(int(linearr[i]), i) for i in range(len(linearr)) if linearr[i] is not "x"]

n, a = [], []
for line in buslines:
  n.append(line[0])
  a.append(line[0] - line[1])

print(chinese_remainder(n, a))
