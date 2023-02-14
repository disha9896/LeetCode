class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hashset = set()
        for val in nums:
            if val in hashset:
                return True
            hashset.add(val)
        return False
