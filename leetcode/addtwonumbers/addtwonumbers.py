# https://leetcode.com/problems/add-two-numbers/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        result = ListNode(0)
        current = result
        carryover = 0
        while l1 or l2:
            current_sum = carryover
            if l1:
                current_sum += l1.val
                l1 = l1.next
            if l2:
                current_sum += l2.val
                l2 = l2.next
            if current_sum >= 10:
                carryover = 1
            else:
                carryover = 0
            val = current_sum % 10
            current.next = ListNode(val)
            current = current.next

        if carryover == 1:
            current.next = ListNode(1)
            current = current.next
            
        return result.next

if __name__ == '__main__':
    a, a.next, a.next.next = ListNode(2), ListNode(4), ListNode(3)
    b, b.next, b.next.next = ListNode(5), ListNode(6), ListNode(4)
    result = Solution().addTwoNumbers(a, b)
    print ("{0} -> {1} -> {2}".format(result.val, result.next.val, result.next.next.val))