# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # two pointers
        # currently one points at null 
        duplicates = set()
        distinct = set()

        current = head
        while current != None:
            if current.val in distinct:
                duplicates.add(current.val)
            else:
                distinct.add(current.val)
            current = current.next
        outputSet = distinct-duplicates

        output = ListNode()
        currentOut = output

        current = head
        while current != None:
            if current.val in outputSet:
                currentOut.next = current
                currentOut = currentOut.next
            current = current.next
        currentOut.next = None
        return output.next


        