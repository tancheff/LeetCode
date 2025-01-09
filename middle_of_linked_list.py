# Definition for singly-linked list.
# [1,2,3,4,5]

# Input: head = [1,2,3,4,5]
# Output: [3,4,5]
# Explanation: The middle node of the list is node 3.
# from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

new_node = ListNode(1)
new_node.next = ListNode(2)
new_node.next.next = ListNode(3)
new_node.next.next.next = ListNode(4)
new_node.next.next.next.next = ListNode(5)


node_list = []
current_node = new_node

while True:
    if current_node is None:
        break
    else:
        node_list.append(current_node.val)

    current_node = current_node.next



class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node_list = []
        current_node = head

        while True:
            if current_node is None:
                break
            else:
                node_list.append(current_node)

            current_node = current_node.next

        return node_list[len(node_list) // 2]

solution = Solution()

print(solution.middleNode(new_node))





