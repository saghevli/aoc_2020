# must include preamble length in filename
import sys, re, heapq

def findFirstInvalid(nums):
  for i in range(preamble, len(nums)):
    if not twoNumsSumToN(nums[i-preamble:i], nums[i]):
      return nums[i]

def twoNumsSumToN(nums, n):
  for i in range(len(nums)):
    if n - nums[i] in nums:
        return True
  return False

def searchForContiguousSubseq(nums, s):
  for i in range(len(nums)-1):
    sum = nums[i]
    for j in range(i+1, len(nums)):
      if sum > found:
        break
      if sum == found:
        return max(nums[i:j]) + min(nums[i:j])
      sum += nums[j]

preamble = int(re.findall("([0-9]+)", sys.argv[1])[0])
nums = [int(l) for l in open(sys.argv[1]).read().split("\n")]
found = findFirstInvalid(nums)
print("invalid: " + str(found))
print(searchForContiguousSubseq(nums, found))
