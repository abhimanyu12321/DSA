class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        count = defaultdict(int)
        for i in s:
            count[i]+=1
        for i in t:
            count[i]+=1
        print(count)
        for key in count:
            if count[key] % 2 != 0:
                return key
        
        