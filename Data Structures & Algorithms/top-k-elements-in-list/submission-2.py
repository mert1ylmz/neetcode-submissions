import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_Dict = Counter(nums)
        
    
        return heapq.nlargest(k, count_Dict, key = count_Dict.get)