# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def store(head, arr):
            if not head:
                return
            arr.append(head.val)
            store(head.next, arr)
        
        def reversee(head, arr, i):
            if i*(-1) <= len(arr):
                head.val = arr[i]
                reversee(head.next, arr, i-1)
            
        arr = []
        i = -1
        store(head, arr)
        reversee(head, arr, i)
        return head