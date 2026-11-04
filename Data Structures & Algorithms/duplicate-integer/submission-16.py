class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hectorGay = set()

        for n in nums:
            if n in hectorGay:
                return True
            hectorGay.add(n)
        return False
            