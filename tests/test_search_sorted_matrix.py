import pytest
from src.search_sorted_matrix import search_matrix

def test_search_matrix_basic_success():
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
    ]
    assert search_matrix(matrix, 3) == True
    assert search_matrix(matrix, 13) == False

def test_search_matrix_edge_cases():
    # Empty matrix
    assert search_matrix([], 5) == False
    
    # Single row matrix
    matrix_single_row = [[1, 3, 5]]
    assert search_matrix(matrix_single_row, 3) == True
    assert search_matrix(matrix_single_row, 4) == False

    # Single column matrix
    matrix_single_col = [[1], [3], [5]]
    assert search_matrix(matrix_single_col, 3) == True
    assert search_matrix(matrix_single_col, 4) == False

def test_search_matrix_boundary_values():
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
    ]
    # First and last elements
    assert search_matrix(matrix, 1) == True
    assert search_matrix(matrix, 60) == True

def test_search_matrix_invalid_inputs():
    # Not a list of lists
    with pytest.raises(TypeError):
        search_matrix(None, 5)
    
    with pytest.raises(TypeError):
        search_matrix([1, 2, 3], 5)
    
    # Non-integer target
    with pytest.raises(TypeError):
        search_matrix([[1, 2], [3, 4]], "5")

def test_search_matrix_inconsistent_rows():
    # Inconsistent row lengths
    with pytest.raises(ValueError):
        search_matrix([[1, 2], [3, 4, 5]], 5)

def test_search_matrix_advanced_scenarios():
    # Large matrix with multiple possible locations
    large_matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    assert search_matrix(large_matrix, 5) == True
    assert search_matrix(large_matrix, 20) == False

def test_search_matrix_negative_numbers():
    matrix_with_negatives = [
        [-10, -5, 0],
        [1, 3, 5],
        [10, 15, 20]
    ]
    assert search_matrix(matrix_with_negatives, -5) == True
    assert search_matrix(matrix_with_negatives, -7) == False