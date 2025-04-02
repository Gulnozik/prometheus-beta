class Node:
    """
    A class representing a node in a singly linked list.
    
    Attributes:
        val (Any): The value stored in the node
        next (Node, optional): Reference to the next node in the list
    """
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class LinkedList:
    """
    A class representing a singly linked list with utility methods.
    
    Attributes:
        head (Node, optional): The first node in the linked list
    """
    def __init__(self, values=None):
        """
        Initialize a linked list, optionally from a list of values.
        
        Args:
            values (list, optional): Initial values to populate the linked list
        """
        self.head = None
        if values:
            for val in reversed(values):
                self.insert_at_head(val)
    
    def insert_at_head(self, val):
        """
        Insert a new node at the head of the linked list.
        
        Args:
            val (Any): Value to be inserted
        """
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

def is_palindrome(head):
    """
    Determine if a linked list is palindromic.
    
    Args:
        head (Node): The head of the linked list
    
    Returns:
        bool: True if the linked list is palindromic, False otherwise
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    # Handle empty list or single element list
    if not head or not head.next:
        return True
    
    # Find the middle of the linked list
    slow = fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    
    # Reverse the second half of the list
    second_half = slow.next
    prev = None
    while second_half:
        temp = second_half.next
        second_half.next = prev
        prev = second_half
        second_half = temp
    
    # Compare the first and reversed second half
    first_half = head
    second_half = prev
    while second_half:
        if first_half.val != second_half.val:
            return False
        first_half = first_half.next
        second_half = second_half.next
    
    return True