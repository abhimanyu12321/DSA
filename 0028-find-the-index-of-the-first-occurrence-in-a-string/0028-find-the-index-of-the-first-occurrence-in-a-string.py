class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        left,right,temp = 0,0,''

        while left < len(haystack) and right <len(needle):
            if haystack[left] == needle[right]:
                temp+= haystack[left]
                left+=1
                right+=1
            else:
                temp = ''
                left = left-right+1
                right = 0
            if temp == needle:
                return left-len(needle)
        return -1
        


        