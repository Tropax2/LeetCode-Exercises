# Terribly explained exercise, this code returns the list without duplicates and its length.

class Solution:
    def removeDuplicates(self, nums):
        self.nums = nums 
        self.noduplicates = []

        for i in range(len(self.nums)):
            if self.nums[i] not in self.noduplicates:
                self.noduplicates.append(self.nums[i])
            
        return len(self.noduplicates), self.noduplicates

 
