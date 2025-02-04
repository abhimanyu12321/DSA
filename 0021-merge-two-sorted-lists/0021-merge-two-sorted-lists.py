# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        ans = ListNode(-1100)
        ref = ans 
        while list1 and list2:
            if list2.val <= list1.val:
                ans.next = ListNode(list2.val)
                list2 = list2.next
                ans = ans.next
            else:
                ans.next = ListNode(list1.val)
                list1 = list1.next
                ans = ans.next
        while list1:
            ans.next = ListNode(list1.val)
            list1 = list1.next
            ans = ans.next
        while list2:
            ans.next = ListNode(list2.val)
            list2 = list2.next
            ans = ans.next

        return ref.next
                
        