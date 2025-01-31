class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # ans = []
        # for i in range(len(nums)):
        #     left = target - nums[i]
        #     for j in range(i+1,len(nums)):
        #         if left == nums[j]:
        #             ans.append(i)
        #             ans.append(j)
        #             return ans
        
        # optimized
        ans = []
        store = {}
        for i in range(len(nums)):  
            left = target - nums[i]
            if left in store:
                ans.append(store[left])
                ans.append(i)
                return ans
            store[nums[i]] = i

        
        