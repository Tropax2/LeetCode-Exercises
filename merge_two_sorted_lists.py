class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list_1, list_2):
        placeholder = ListNode()
        current = placeholder

        while list_1 and list_2:
            if list_1.val > list_2.val:
                current.next = list_2
                list_2 = list_2.next

            else:
                current.next = list_1
                list_1 = list_1.next
            
            current = current.next
        
        if list_1:
            current.next = list_1

        elif list_2:
            current.next = list_2
        
        return placeholder.next

 