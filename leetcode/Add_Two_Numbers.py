# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curl1 = l1
        curl2 = l2
        dummy = ListNode(0)
        curr = dummy

        carry = 0
        while curl1 != None or curl2 != None or carry != 0:
            v1 = getattr(curl1, 'val', 0)
            v2 = getattr(curl2, 'val', 0)
            s = carry + v1 + v2
            carry = s // 10
            curr.next = ListNode(s % 10)
            curr = curr.next
            curl1 = curl1.next if curl1 else None
            curl2 = curl2.next if curl2 else None
        return dummy.next



