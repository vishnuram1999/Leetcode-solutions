class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head,n):
    def traverse(head, arr):
        if not head:
            return
        arr.append(head.val)
        traverse(head.next, arr)
        
        
    def remove(head, index, newhead, count, length):
        #print(count)
        if not head:
            return
        if count == index:
            head = head.next
            count += 1
        newhead.val = head.val
        #print(count)
        if head.next:
            print(count)
            
            newhead.next = ListNode()
            remove(head.next, index, newhead.next, count+1, length)
            
    arr = []
    traverse(head, arr)
    length = len(arr)
    index = length - n 
    newhead = ListNode()
    count = 0
    remove(head, index, newhead, count, length)
    return newhead

head= ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

removeNthFromEnd(head, 2)
    
        
        