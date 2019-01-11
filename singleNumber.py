import random
from random import shuffle

nums = list(range(1, 10))
single_element = random.choice(nums)
nums.remove(single_element)
nums = [val for val in nums for _ in (0, 1)]
nums.append(single_element)
shuffle(nums)

print("Single element", single_element)
print("List:", nums)

def singleNumber(nums):
    res = 0
    for num in nums:
        print("num ", num)
        print("res ", res)
        res ^= num
    return res

res = singleNumber(nums)
print("Result", res)
