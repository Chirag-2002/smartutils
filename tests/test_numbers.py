from smartutils.numbers import NumberUtility

def test_is_even():
    assert NumberUtility(10).is_even() == True

def test_check_sign():
    assert NumberUtility(-5).check_sign() == "negative"

def test_leap_year():
    assert NumberUtility(2024).is_leap_year() == True
