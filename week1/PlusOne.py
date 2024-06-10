class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1]<9:
            digits[-1]+=1
        else:
            if len(digits)==1:
                digits=[1,0]
            else:
                digits=self.plusOne(digits[:-1])+[0]
        return digits