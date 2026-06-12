class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       si = Counter(s)

       ti = Counter(t)

       return si == ti
