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

#Chart Type Test - Should be 1 or 2
@pytest.mark.parametrize("chart_input,expected", [
    ("1", True),
    ("2", True),
    ("3", False),
    ("0", False),
    ("a", False),
])
def test_chart_type_input(chart_input, expected):
    assert chart_input in ["1", "2"] == expected