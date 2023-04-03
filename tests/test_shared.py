import sys
sys.path.append('.')
import shared as sh
import pytest

def test_clean_string():
    test_str = " This! is      a ,test string  "

    assert "This is a test string" == sh.clean_string(test_str), "String <{}> not cleaned as expected".format(test_str)

def test_space_compress():
    test_str = "Test \n string  "

    assert "Test string" == sh.space_compress(test_str), "String <{}> not compressed as expected".format(test_str)

@pytest.mark.xfail
def test_asserts_fail():
    test_str = "Test \n string  "

    assert "Test, string" == sh.space_compress(test_str), "String <{}> not compressed as expected".format(test_str)

@pytest.mark.skip(reason="no way of currently testing this")
def test_asserts_skipping():
    test_str = "Test \n string  "

    assert "Test, string" == sh.space_compress(test_str), "String <{}> not compressed as expected".format(test_str)

@pytest.mark.skipif(sys.platform != 'darwin', reason="requires the darwin platform")
def test_asserts_skipif_onlyondarwin():
    test_str = "Test \n string  "
    print("My platform is", sys.platform) ## We do not see a print out
    assert "Test string" == sh.space_compress(test_str), "String <{}> not compressed as expected".format(test_str)

# @pytest.mark.skipif(sys.platform == 'darwin', reason="requires the darwin platform")
# def test_asserts_skipif_fail_onlynotondarwin():
#     test_str = "Test \n string  "

#     print("My platform is", sys.platform) ## We do not see a print out
#     assert "Test, string" == sh.space_compress(test_str), "String <{}> not compressed as expected".format(test_str)