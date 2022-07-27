def changeArr(start, end, newArr, arr):
    for i in range(len(arr)):
        if (i)%2 == 0:
            newArr.append(arr[start])
            start += 1
        else:
            newArr.append(arr[end])
            end -= 1
            

arr = [1,2,3,4,5]
newArr = []
start = 0
end = -1
changeArr(start, end, newArr, arr)
print(newArr)# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def order(head, arr):
            if not head:
                return
            arr.append(head.val)
            order(head.next, arr)
        
        def changeArr(start, end, newArr, arr):
            for i in range(len(arr)):
                if (i)%2 == 0:
                    newArr.append(arr[start])
                    start += 1
                else:
                    newArr.append(arr[end])
                    end -= 1
                             
        def updateLinkedList(head, newArr, i):
            if i < len(newArr):
                head.val = newArr[i]
                updateLinkedList(head.next, newArr, i+1)
        
        arr = []
        order(head, arr)
        newArr = []
        start = 0
        end = -1
        changeArr(start, end, newArr, arr)
        updateLinkedList(head, newArr, 0)
        
        