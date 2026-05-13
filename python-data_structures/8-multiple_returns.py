#!/usr/bin/python3
def multiple_returns(sentence):
    # Check if the sentence is empty
    if len(sentence) == 0:
        # If empty, return length 0 and None as first character
        return (0, None)
    else:
        # Return the length of the sentence
        # and the first character of the sentence
        return (len(sentence), sentence[0])
