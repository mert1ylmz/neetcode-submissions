class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = list(s)
        b = list(t)
        
        if len(a) != len(b):
            return False
        if sorted(a) == sorted(b):
            return True
        else:
            return False
            
        