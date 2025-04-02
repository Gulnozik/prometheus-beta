import pytest
from src.array_common_element import has_common_element

def test_common_element_exists():
    """Test when a common element exists"""
    arr1 = [1, 2, 3, 4]
    arr2 = [4, 5, 6, 7]
    assert has_common_element(arr1, arr2) == True

def test_no_common_element():
    """Test when no common element exists"""
    arr1 = [1, 2, 3]
    arr2 = [4, 5, 6]
    assert has_common_element(arr1, arr2) == False

def test_empty_arrays():
    """Test when one or both arrays are empty"""
    arr1 = []
    arr2 = [1, 2, 3]
    assert has_common_element(arr1, arr2) == False
    assert has_common_element(arr2, arr1) == False
    assert has_common_element([], []) == False

def test_common_with_duplicates():
    """Test when common elements are duplicates"""
    arr1 = [1, 2, 2, 3]
    arr2 = [3, 4, 4]
    assert has_common_element(arr1, arr2) == True

def test_different_types():
    """Test with arrays of different types"""
    arr1 = [1, 'a', 2]
    arr2 = ['a', 3, 4]
    assert has_common_element(arr1, arr2) == True

def test_invalid_input_types():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError):
        has_common_element(1, [1, 2, 3])
    
    with pytest.raises(TypeError):
        has_common_element([1, 2, 3], "not a list")
    
    with pytest.raises(TypeError):
        has_common_element(None, [1, 2, 3])