class Solution:

    def __init__(self):
        self.result = []

    def twoSum(self, nums, target):
        self.nums = nums 
        self.target = target
        for i in range(len(self.nums)):
            c = target - self.nums[i]
            if c in nums and i != nums.index(c):
                self.result.append(i) 
                self.result.append(nums.index(c))
                break     
        return self.result
    


