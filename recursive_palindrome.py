def clean_string(unclean):
    '''Removes special characters in a string

    Args: 
        string (str) text

    Returns:
        None
        List of (list) lowercase letters

    '''
    letters = "abcdefghijklmnopqrstuvwxyz"

    clean = [letter for letter in unclean if letter.lower() in letters]

    if not clean:
        return None

    return clean


def recursive_palindrome(text):
    pass


def main():
    pass


case = "A man, a plan, a canal, Panama."
print(len("AmanaplanacanalPanama"))
#print(clean_string(case))
print(len(clean_string(case)))