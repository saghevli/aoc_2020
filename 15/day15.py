import sys, collections
nums = [int(n) for n in open(sys.argv[1]).read().split(",")]
def f():
  return collections.deque([-1, -1], maxlen=2)
spoken = collections.defaultdict(f)
for i, n in enumerate(nums):
  spoken[n].append(i)

i = len(nums)
end = 30000000
while i < end:
  speak = 0
  if spoken[nums[-1]][0] != -1:
    speak = spoken[nums[-1]][1] - spoken[nums[-1]][0]
  nums.append(speak)
  spoken[speak].append(i)
  i += 1

print(nums[end-1])


