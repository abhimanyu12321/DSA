class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        count = defaultdict(int)

        for i in s:
            count[i]+=1
        for i in t:
            count[i]-=1
        for key in count:
            if count[key] != 0:
                return False
        return True        