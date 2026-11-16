class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       
        count = [0] * 26
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            count[ord('a') - ord(s[i])] += 1
            count[ord('a') - ord(t[i])] -= 1

        for val in count:
            if val != 0:
                return False
        return True