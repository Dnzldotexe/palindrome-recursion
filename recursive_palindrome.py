'''
This python module contains three functions:
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
    letters = "abcdefghijklmnopqrstuvwxyz"                  # Creates a string of lowercase alphabet

    # Compares each element in the string to lowercase alphabet then stores it in a list
    clean = [letter.lower() for letter in unclean if letter.lower() in letters]

    if not clean:                                           # Returns None if empty
        return None

    return clean                                            # Returns the cleaned list


def recursive_palindrome(text):
    '''Determines if a string is palindrome recursively

    Args: 
        list (list) of characters

    Returns:
        True
        False

    '''
    if len(text) < 2:                                       # Base case, returns True
        print("String is a Palindrome.")                    # when list is less than two
        return True

    if text[0] != text[-1]:                                 # Base case, returns False
        print("String is not a Palindrome.")                # when first and last element
        return False                                        # are not equal

    return recursive_palindrome(text[1:-1])                 # Slice the list then recurse


def main():
    '''Demonstrates the recursive_palindrome() function

    '''
    while True:                                             # Loops until input is empty
        words = input("\nIs it a palindrome: ").strip()

        if not words:                                       # Returns when input is empty
            return None

        words = clean_string(words)                         # Cleans the string
        result = recursive_palindrome(words)                # Stores the result of the function call

        print(f"Result: {result}.")                         # Prints the result


main()                                                      # Runs the function
