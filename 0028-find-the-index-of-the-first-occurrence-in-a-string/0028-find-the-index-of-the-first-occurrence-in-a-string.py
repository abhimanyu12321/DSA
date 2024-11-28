class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        size = len(needle)
        for i in range(len(haystack)-size+1):
            str = haystack[i:i+size]
            if str == needle:
                return i
        return -1
        