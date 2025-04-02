import pytest
from src.linked_list_palindrome import LinkedList, is_palindrome, Node

def test_empty_list():
    """Test that an empty list is considered a palindrome"""
    empty_list = LinkedList()
    assert is_palindrome(empty_list.head) == True

def test_single_element_list():
    """Test that a single-element list is a palindrome"""
    single_list = LinkedList([5])
    assert is_palindrome(single_list.head) == True

def test_palindrome_even_length():
    """Test a palindrome with even number of elements"""
    palindrome_list = LinkedList([1, 2, 2, 1])
    assert is_palindrome(palindrome_list.head) == True

def test_palindrome_odd_length():
    """Test a palindrome with odd number of elements"""
    palindrome_list = LinkedList([1, 2, 3, 2, 1])
    assert is_palindrome(palindrome_list.head) == True

def test_non_palindrome_even_length():
    """Test a non-palindrome with even number of elements"""
    non_palindrome_list = LinkedList([1, 2, 3, 4])
    assert is_palindrome(non_palindrome_list.head) == False

def test_non_palindrome_odd_length():
    """Test a non-palindrome with odd number of elements"""
    non_palindrome_list = LinkedList([1, 2, 3, 4, 5])
    assert is_palindrome(non_palindrome_list.head) == False

def test_palindrome_with_repeated_elements():
    """Test a palindrome with repeated elements"""
    palindrome_list = LinkedList([1, 1, 1, 1])
    assert is_palindrome(palindrome_list.head) == True

def test_palindrome_large_values():
    """Test a palindrome with larger values"""
    palindrome_list = LinkedList([100, 200, 300, 200, 100])
    assert is_palindrome(palindrome_list.head) == True