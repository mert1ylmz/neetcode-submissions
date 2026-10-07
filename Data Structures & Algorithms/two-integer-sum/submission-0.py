class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            is_target = target - num
            if is_target in seen:
                return [seen[is_target], i]
            seen[num] = i