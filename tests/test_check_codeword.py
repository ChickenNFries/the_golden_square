from lib.check_codeword import *

def test_check_codeword_returns_correct_answer():
    result = check_codeword("horse")

    assert result == "Correct! Come in."

def test_check_codeword_returns_close_answer():
    result = check_codeword("hike")

    assert result == "Close, but nope."

def test_check_codeword_returns_wrong_answer():
    result = check_codeword("pony")

    assert result == "Wrong!"