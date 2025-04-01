import pytest
from src.anagram_checker import are_anagrams

def test_basic_anagrams():
    """Test basic anagram scenarios"""
    assert are_anagrams('listen', 'silent') == True
    assert are_anagrams('hello', 'olleh') == True

def test_non_anagrams():
    """Test non-anagram scenarios"""
    assert are_anagrams('hello', 'world') == False
    assert are_anagrams('python', 'java') == False

def test_case_insensitive():
    """Test case-insensitive anagram checking"""
    assert are_anagrams('Tea', 'Eat') == True
    assert are_anagrams('SILENT', 'listen') == True

def test_whitespace_handling():
    """Test anagram checking with whitespace"""
    assert are_anagrams('debit card', 'bad credit') == True
    assert are_anagrams('a gentleman', 'elegant man') == True

def test_empty_strings():
    """Test empty string scenarios"""
    assert are_anagrams('', '') == True

def test_different_lengths():
    """Test strings of different lengths"""
    assert are_anagrams('hello', 'hello world') == False

def test_type_errors():
    """Test error handling for incorrect input types"""
    with pytest.raises(TypeError):
        are_anagrams(123, 'hello')
    with pytest.raises(TypeError):
        are_anagrams('hello', None)
    with pytest.raises(TypeError):
        are_anagrams(None, None)