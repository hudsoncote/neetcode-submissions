class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sContains = sorted(list(s))
        tContains = sorted(list(t))

        return sContains == tContains and len(s) == len(t)