# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # simle problem take the mod
        # make the next one the new head break the old connection
        # add to end
        # return

        # pull it from the back 2   
        # figure out how long the list is
        if head == None:
            return head
        
        if k == 0:
            return head

        length = 0
        current = head
        backNode = None
        while current != None:
            if current.next == None:
                backNode = current
            current = current.next
            length += 1
        
        translated = k % length
        if translated == 0:
            return head

        newEndnum = length - translated - 1 # becomes new back

        count = 0
        current = head
        while count < newEndnum:
            current = current.next
            count += 1

        oldHead = head
        head = current.next
        current.next = None
        backNode.next = oldHead

        return head
