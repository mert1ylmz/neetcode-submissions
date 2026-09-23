class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_Set = set(nums)
        if len(nums)>len(nums_Set):
            return True
        else:
            return False
        

