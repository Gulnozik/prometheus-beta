def search_matrix(matrix, target):
    """
    Search for a target value in a 2D matrix with sorted inner lists.
    
    Args:
        matrix (List[List[int]]): A 2D matrix where inner lists are sorted 
                                  in ascending order.
        target (int): The value to search for in the matrix.
    
    Returns:
        bool: True if the target exists in the matrix, False otherwise.
    
    Time Complexity: O(m * log n), where m is the number of rows and n is the number of columns
    Space Complexity: O(1)
    
    Raises:
        TypeError: If matrix is not a list of lists or target is not an integer
        ValueError: If matrix is empty or contains inconsistent row lengths
    """
    # Validate input
    if not isinstance(matrix, list) or not matrix:
        return False
    
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("Matrix must be a list of lists")
    
    if not isinstance(target, int):
        raise TypeError("Target must be an integer")
    
    # Check for consistent row lengths
    row_lengths = set(len(row) for row in matrix)
    if len(row_lengths) > 1:
        raise ValueError("All rows must have the same length")
    
    # Perform binary search on each row
    for row in matrix:
        # Optimize: skip rows that can't contain the target
        if row and (target < row[0] or target > row[-1]):
            continue
        
        # Binary search within the row
        left, right = 0, len(row) - 1
        while left <= right:
            mid = (left + right) // 2
            if row[mid] == target:
                return True
            elif row[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
    
    return False