class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start ,end = 0,len(nums)-1
        while start <= end:
            mid = int((start+end)/2)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid-1
            else: start = mid+1
        return -1
        