def is_match(text, pattern):
    """
    This is a recursive function that determines whether a given text string matches a specified pattern. It recursively compares characters between the text and pattern.
    The function return a match if both the text and pattern are empty and no match if there is text and no pattern.
    """
    # If the pattern is empty and also the text is empty the match is successful. The match not successful if the pattern is empty and text is not empty.
    if not pattern:
        return not text
    
    # Check between text and pattern of the first characters if the match.
    first_character_match = bool(text) and pattern[0] in {text[0], '.'}

    # Check if the pattern has two characters and the first is asterisk
    # Condition True thus the asterisk and preceding character is zero.
    if len(pattern) >= 2 and pattern[1] == '*':

        # Case asterisk
        # Case 1 ignore the character and asterisk(zero) and continue 
        # Case 2 First match continue and remove the first character in the pattern
        return is_match(text, pattern[2:]) or (first_character_match and is_match(text[1:], pattern))
    else:
        return first_character_match and is_match(text[1:], pattern[1:]) # Checking the match between text and pattern in the first character, True continue
    
print(is_match("aab", "c*a*b"))  # Display the output
