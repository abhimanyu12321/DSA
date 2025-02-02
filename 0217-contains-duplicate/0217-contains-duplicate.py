class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = defaultdict(int)
        for i in nums:
            if i in count:
                return True
            count[i]+=1
        # for i in count.values():
        #     if i > 1:
        #         return True

        return False
        