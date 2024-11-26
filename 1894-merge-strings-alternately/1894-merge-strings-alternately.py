class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        w1,w2,turn = 0,0,0
        ans= ''
        while w1<len(word1) and w2<len(word2):
            if turn%2 == 0:
                ans+=word1[w1]
                w1+=1
                turn+=1
            else:
                ans+= word2[w2]
                w2+=1
                turn+=1
        if w1<len(word1):
            ans = ans + word1[w1:]
        if w2<len(word2):
            ans = ans + word2[w2:]
        return ans


        