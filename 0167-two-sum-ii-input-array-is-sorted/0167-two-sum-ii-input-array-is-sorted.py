class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # BRUTE FORCE TIME CMPLEXITY 0(N*N)
        # ans = []
        # for i in range(len(numbers)):
        #     sum = 0
        #     for j in range(i+1,len(numbers)):
        #         sum = numbers[i]+numbers[j]
        #         if sum == target:
        #             ans.append(i+1)
        #             ans.append(j+1)
        #             return ans
        # return ans
        ans = []
        start = 0
        end = len(numbers)-1
        while start < end:
            sum = numbers[start]+numbers[end]
            if sum > target:
                end-=1
            elif sum < target:
                start+=1
            else:
                ans.append(start+1)
                ans.append(end+1)
                return ans
            


        