# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 or not list2:
            if not list1:
                return list2
            else:
                return list1
    
        def findGreat(list1, list2, ans):
            if list1 != None and list2 != None:
                if list1.val < list2.val:
                    ans.val = list1.val
                    list1 = list1.next
                elif list2.val < list1.val:
                    ans.val = list2.val
                    list2 = list2.next
                else:
                    ans.val = list1.val
                    list1 = list1.next
                ans.next = ListNode()
                findGreat(list1, list2, ans.next)
            if list1 and list2 == None:
                ans.next = list1
            if list2 and list1 == None:
                ans.next = list2
                
        ans = ListNode()
        findGreat(list1, list2, ans)
        
        return ans
        
        
        
        
            
        