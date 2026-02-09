from lib.counter import *

def _test_counter_can_count():
    counter = Counter()
    counter.add(2)
    result = counter.report()

    assert result == "Counted to 2 so far."