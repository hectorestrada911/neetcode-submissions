class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        constS, constT = {}, {}

        for i in range(len(s)):
            constS[s[i]] = 1 + constS.get(s[i], 0)
            constT[t[i]] = 1 + constT.get(t[i], 0)

        return constS == constT
            