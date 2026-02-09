from lib.report_length import *

#if the person adds a string word

def test_report_length_returns_length():
    result = report_length("seven")

    assert result == "This string was 5 characters long."

#If the person does not add a string


def test_report_length_empty_string():

    result = report_length("")

    assert result == "This string was 0 characters long."

    #if the person adds a string with spaces

def test_report_length_spaces_in_string():

    result = report_length("I am tired")

    assert result == "This string was 10 characters long."