class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            pass
        else:
            nums.append(target)
        s=sorted(nums)
        for i in range(len(s)):
            if s[i]==target:
                return i