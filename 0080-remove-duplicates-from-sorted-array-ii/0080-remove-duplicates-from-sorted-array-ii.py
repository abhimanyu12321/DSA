class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = nums[0];
        index = 1
        occurence = 1;
        for i in range(len(nums)):
            if i != 0:
                if nums[i] == temp:
                    if occurence <= 2:
                        nums[index] = nums[i]
                        index+=1
                        occurence+=1
                        
                    occurence+=1

                else:
                    temp = nums[i]
                    nums[index] = nums[i]
                    index+=1
                    occurence = 1

        return index