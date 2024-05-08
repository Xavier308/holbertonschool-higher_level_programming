def islower(c):
    """
    Check if a character is lowercase.
    
    Args:
        c: A character (string of length 1).
        
    Returns:
        True if c is lowercase, False otherwise.
    """
    # Check if the ASCII value of c is between the ASCII values of lowercase 'a' and 'z'
    return ord('a') <= ord(c) <= ord('z')
