class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        temp = s+s
        d = temp[1:len(temp)-1]
        return s in d
        
        
        