import pytest
from src.array_sum import calculate_array_sum

def test_calculate_array_sum_positive_integers():
    """Test sum of positive integers"""
    assert calculate_array_sum([1, 2, 3, 4, 5]) == 15

def test_calculate_array_sum_negative_integers():
    """Test sum of negative integers"""
    assert calculate_array_sum([-1, -2, -3, -4, -5]) == -15

def test_calculate_array_sum_mixed_numbers():
    """Test sum of mixed positive and negative numbers"""
    assert calculate_array_sum([-1, 2, -3, 4, -5]) == -3

def test_calculate_array_sum_floats():
    """Test sum of floating point numbers"""
    assert calculate_array_sum([1.5, 2.5, 3.0]) == 7.0

def test_calculate_array_sum_single_element():
    """Test sum of a single element list"""
    assert calculate_array_sum([42]) == 42

def test_calculate_array_sum_empty_list_raises_error():
    """Test that an empty list raises a ValueError"""
    with pytest.raises(ValueError, match="Cannot calculate sum of an empty list"):
        calculate_array_sum([])

def test_calculate_array_sum_non_list_input_raises_error():
    """Test that non-list input raises a TypeError"""
    with pytest.raises(TypeError, match="Input must be a list"):
        calculate_array_sum("not a list")

def test_calculate_array_sum_non_numeric_elements_raises_error():
    """Test that list with non-numeric elements raises a TypeError"""
    with pytest.raises(TypeError, match="All elements must be numeric"):
        calculate_array_sum([1, 2, "three", 4])

def test_calculate_array_sum_mixed_numeric_types():
    """Test sum of mixed numeric types (int and float)"""
    assert calculate_array_sum([1, 2.5, 3, 4.5]) == 11.0