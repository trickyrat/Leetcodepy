from typing import Optional


class ListNode(object):
    """
    Definition fro singly-linked list.
    """

    def __init__(self, val: int = 0, next: Optional["ListNode"] = None) -> None:
        self.val: int = val
        self.next: Optional[ListNode] = next

    def __lt__(self, other):
        return True if self.val < other.val else False
    
