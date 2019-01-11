import random

def missingNumber(nums):
    sum_first = (nums[0]-1)*((nums[0]-1)+1)//2
    sum_last = nums[-1]*(nums[-1]+1)//2
    sum_nums = sum_last-sum_first
    res = sum_nums - sum(nums)
    print(res)

start_int = random.randint(1, 10)
end_int = random.randint(11, 100)
nums = list(range(start_int, end_int))
nums.remove(random.choice(nums))
print(nums)
missingNumber(nums)
    
