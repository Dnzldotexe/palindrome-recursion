'''
This python module contains three functions.
(1) clean_string()
(2) recursive_palindrome()
(3) main()

'''

def clean_string(unclean):
    '''Removes special characters in a string

    Args: 
        string (str) text

    Returns:
        None
        List of (list) lowercase letters

    '''
    letters = "abcdefghijklmnopqrstuvwxyz"

    clean = [letter.lower() for letter in unclean if letter.lower() in letters]

    if not clean:
        return None

    return clean


def recursive_palindrome(text):
    '''Determines if a string is palindrome recursively

    Args: 
        string (str) text

    Returns:
        True
        False

    '''
    if len(text) < 2:
        print("String is a Palindrome.")
        return True

    if text[0] != text[-1]:
        print("String is not a Palindrome.")
        return False

    return recursive_palindrome(text[1:-1])


def main():
    '''Demonstrates the recursive_palindrome() function
    
    Prints: 
        string (str) text

    '''
    while True:                                             # Loops until input is empty
        words = input("\nIs it a palindrome: ").strip()

        if not words:                                       # Returns when input is empty
            return None

        words = clean_string(words)
        result = recursive_palindrome(words)                # Stores the result of the function call

        print(f"Result: {result}.")                         # Prints the result


main()                                                      # Runs the function
