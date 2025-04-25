import re
import pytest # type: ignore

#Symbol test
@pytest.mark.parametrize("symbol,expected", [
    ("AAPL", True),
    ("GOOG", True),
    ("MSFT123", False),       # has numbers
    ("", False),              # empty
    ("TSLA!", False),         # special characters
    ("TOOLONGSYM", False),    # >7 characters
    ("apple", False),         # lowercase
])
def test_symbol(symbol, expected):
    pattern = r"^[A-Z]{1,7}$"
    assert bool(re.fullmatch(pattern, symbol)) == expected