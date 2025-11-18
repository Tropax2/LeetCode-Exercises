class Solution:
    def lengthOfLastWord(self, s):
        self.s = s 
        self.list_of_words = self.s.split(" ")
        
        if len(self.s) == 1:
            return 1
        
        else:
            for i in range(1, len(self.list_of_words) + 1):
                if len(self.list_of_words[-i]) > 0:
                    return len(self.list_of_words[-i])
                
                else:
                    continue
 
 