class Solution:
    def canJump(self, nums):
        if len(nums)==1:
            print(True)
        elif nums[0]<len(nums):
            pop_ind = nums[0] 
            for i in range(0, pop_ind):
                nums.pop(0)
            if nums[0]!=0:
                self.canJump(nums)
            else:
                print(False)
        else:
            print(False)

leetCode = Solution()
if 0:
    nums = [2,3,1,1,4]
if 1:
    nums = [3,2,1,0,4]
leetCode.canJump(nums)
