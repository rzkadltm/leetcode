"""
Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.

Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3

Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.


Constraints:
The number of nodes in the list is in the range [1, 100].
1 <= Node.val <= 100
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val  # The value stored in the node
        self.next = next  # Pointer to the next node in the list

    def __repr__(self):
        result = []
        current = self
        while current:
            result.append(str(current.val))
            current = current.next
        return " -> ".join(result) + " -> None"


node6 = ListNode(6)
node5 = ListNode(5, node6)
node4 = ListNode(4, node5)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        len_nodes = 0
        current_head = head
        while current_head:
            current_head = current_head.next
            len_nodes += 1

        current_node = 1
        while current_node <= round(len_nodes / 2):
            head = head.next
            current_node += 1
        return head


solution = Solution()
print(solution.middleNode(node1))


class Solution2:
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        mid_nodes = head
        end_nodes = head

        while end_nodes and end_nodes.next:
            mid_nodes = mid_nodes.next
            end_nodes = end_nodes.next.next

        return mid_nodes


solution2 = Solution2()
print(solution2.middleNode(node1))
