class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = {}
        for val in strs:
            sorted_val = ''.join(sorted(val))
            if sorted_val in result:
                result[sorted_val].append(val)
            else:
                result[sorted_val] = [val]
       
        return list(result.values())
