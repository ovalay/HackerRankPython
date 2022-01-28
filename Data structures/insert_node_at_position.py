"""
 Insert Node at the specified position of a linked list
  Node is defined as

 class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

 return back the head of the linked list in the below method.
"""


def InsertNth(head, data, position):
    i = 0
    newNode = SinglyLinkedListNode(data)
    curr = head
    while i is not position - 1:
        curr = curr.next
        i += 1
    prev = curr
    next = curr.next
    prev.next = newNode
    newNode.next = next
    return head
