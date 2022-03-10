import shared as sh
sh.afunction()

def test_multi_spaces():
    assert sh.space_compress('word       word     word') == 'word word word', "Failed multi space"

def test_multi_lines():
    multiline = """
    word
    word
    word
    """
    assert sh.space_compress(multiline) == 'word word word', "Failed multi line"
