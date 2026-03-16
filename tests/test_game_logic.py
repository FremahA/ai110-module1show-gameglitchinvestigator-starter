from logic_utils import check_guess, get_range_for_difficulty

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


# Bug fix: hint direction was reversed — "Too High" incorrectly said "Go HIGHER!"
# and "Too Low" incorrectly said "Go LOWER!"
def test_too_high_message_says_go_lower():
    _, message = check_guess(80, 50)
    assert "LOWER" in message.upper()

def test_too_low_message_says_go_higher():
    _, message = check_guess(20, 50)
    assert "HIGHER" in message.upper()


# Bug fix: secret was cast to str on even attempts, making integer comparison fail.
# Guessing the exact secret on any attempt must always return "Win".
def test_win_with_integer_secret():
    outcome, _ = check_guess(42, 42)
    assert outcome == "Win"

def test_too_high_with_integer_secret():
    # Ensures integer > integer comparison is used (not str > str)
    outcome, _ = check_guess(99, 10)
    assert outcome == "Too High"

def test_too_low_with_integer_secret():
    outcome, _ = check_guess(1, 99)
    assert outcome == "Too Low"


# Bug fix: new-game secret and guess prompt used hardcoded 1-100 instead of the
# difficulty range returned by get_range_for_difficulty.
def test_easy_range():
    low, high = get_range_for_difficulty("Easy")
    assert low == 1
    assert high == 20

def test_normal_range():
    low, high = get_range_for_difficulty("Normal")
    assert low == 1
    assert high == 100

def test_hard_range():
    low, high = get_range_for_difficulty("Hard")
    assert low == 1
    assert high == 200


# Edge case tests: Ensure the game handles negative numbers, high-precision decimals, and extremely large values gracefully.

def test_parse_negative_number():
    from logic_utils import parse_guess
    ok, guess, err = parse_guess("-5")
    assert ok is True
    assert guess == -5
    assert err is None

def test_parse_high_precision_decimal():
    from logic_utils import parse_guess
    ok, guess, err = parse_guess("3.999999999999999999")
    assert ok is True
    assert guess == 4
    assert err is None

def test_parse_extremely_large_number():
    from logic_utils import parse_guess
    large_num_str = str(10**1000)  # 1 followed by 1000 zeros
    ok, guess, err = parse_guess(large_num_str)
    assert ok is True
    assert guess == 10**1000
    assert err is None

def test_check_guess_with_negative():
    outcome, message = check_guess(-5, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message.upper()

def test_check_guess_with_large_number():
    outcome, message = check_guess(10**1000, 50)
    assert outcome == "Too High"
    assert "LOWER" in message.upper()



