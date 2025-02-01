class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # Brute force
        # ans = 0
        # for i in range(len(prices)-1):
        #     maxProfit = max(prices[i+1:]) - prices[i]
        #     ans = max(ans,maxProfit)
        # return 0 if ans<0 else ans

        # Optimized
        ans , minValue = 0,prices[0]
        for i in prices:
             ans = max(ans,i-minValue)
             minValue = min(i,minValue)
        return ans

        