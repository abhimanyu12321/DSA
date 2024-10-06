class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        str = {}

        for i in s:
            if str.get(i):
                str[i]+=1
            else:
                str[i] = 1

        for i in t:
            if str.get(i):
                str[i]-=1
            else:
                return False
        
        for key in str.keys():
            if str[key] != 0:
                return False
        return True
        
        