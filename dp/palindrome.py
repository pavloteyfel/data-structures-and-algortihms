def is_palindrome(string):
    """Palindrome recursive version"""
    if len(string) < 2:
        return True

    if string[0] == string[-1]:
        return is_palindrome(string[1:-1])

    return False


assert is_palindrome("racecar") == True
assert is_palindrome("") == True
assert is_palindrome("a") == True
assert is_palindrome("notpalindrome") == False
