class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        DictS, DictT = {}, {}

        for i in range(len(s)):
            DictS[s[i]] = 1 + DictS.get(s[i], 0)
            DictT[t[i]] = 1 + DictT.get(t[i], 0)
        return DictS == DictT
