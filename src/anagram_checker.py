def are_anagrams(str1: str, str2: str) -> bool:
    """
    Check if two strings are anagrams of each other.

    An anagram is a word or phrase formed by rearranging the letters of another word or phrase,
    using all the original letters exactly once.

    Args:
        str1 (str): The first string to compare
        str2 (str): The second string to compare

    Returns:
        bool: True if the strings are anagrams, False otherwise

    Examples:
        >>> are_anagrams('listen', 'silent')
        True
        >>> are_anagrams('hello', 'world')
        False
    """
    # Check if inputs are strings
    if not (isinstance(str1, str) and isinstance(str2, str)):
        raise TypeError("Both inputs must be strings")
    
    # Convert to lowercase and remove whitespace
    str1 = str1.lower().replace(' ', '')
    str2 = str2.lower().replace(' ', '')
    
    # Quick length check
    if len(str1) != len(str2):
        return False
    
    # Use character counting method
    return sorted(str1) == sorted(str2)