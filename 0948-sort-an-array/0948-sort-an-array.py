class Solution(object):

    def Merge(self,array,left,right,mid):
        leftArray = array[left:mid+1]
        rightArray = array[mid+1:right+1]
       
        # Merge above two sorted arrays
        leftIndex , rightIndex,index = 0,0,left
        while leftIndex < len(leftArray) and rightIndex < len(rightArray):
            if leftArray[leftIndex] < rightArray[rightIndex]:
                array[index] = leftArray[leftIndex]
                leftIndex+=1
            else:
                array[index] = rightArray[rightIndex]
                rightIndex+=1
            index+=1
        
        # Add the remaining element into merge array also
        while leftIndex < len(leftArray):
            array[index] = leftArray[leftIndex]
            leftIndex+=1
            index+=1
        while rightIndex < len(rightArray):
            array[index] = rightArray[rightIndex]
            rightIndex+=1
            index+=1


    def MergSort(self,array,left,right,mid):
        if left >= right:
            return
        self.MergSort(array,left,mid,(left+mid)/2)
        self.MergSort(array,mid+1,right,(mid+right+1)/2)
        self.Merge(array,left,right,mid)

    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        self.MergSort(nums,0,(len(nums))-1,((len(nums))-1)/2)
        return nums