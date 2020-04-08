"""
Prompt:
Given a non-empty, singly linked list with head node head, return a middle node of linked list.

If there are two middle nodes, return the second middle node.
"""

# Runs in O(n) time and O(1) space. Completed with two pointer strategy


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def middle_node(head):
    if head == None:
        return head
    first_ptr = head
    second_ptr = head
    while second_ptr.next != None:
        first_ptr = first_ptr.next
        if second_ptr.next.next == None:
            return first_ptr
        second_ptr = second_ptr.next.next
    return first_ptr


def get_linked_list(head):
    node_list = []
    cur_node = head
    while cur_node != None:
        node_list.append(cur_node.val)
        cur_node = cur_node.next
    return node_list


# Test Case
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print(get_linked_list(middle_node(node1)))  # [1,2,3,4,5] -> [3,4,5]

node6 = ListNode(6)

node5.next = node6

print(get_linked_list(middle_node(node1)))  # [1,2,3,4,5,6] -> [4,5,6]
