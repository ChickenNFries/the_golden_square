from lib.reminder import *

def test_reminds_the_user_to_do_a_task():
    reminder = Reminder("Kay")
    reminder.remind_me_to("Walk the dog")
    result = reminder.remind()

    assert result == "Walk the dog, Kay!"

    """Rather than our example being to call one method and check the return value, 
    our example involves calling a number of methods that exercise the intended behaviour 
    of the class."""

    