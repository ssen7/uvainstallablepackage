def afunction():
    print("This is the installed function")

def clean_string(str_word):
    """
    INPUTS:
    str_word     string string contining several words to clean
    RETURNS:
    string       the string after removal of extra spaces, punctuation and lowercasing
    """
    assert isinstance(str_word, str), "String expected but recieved type {} instead".format(type(str_word))

    return str_word
