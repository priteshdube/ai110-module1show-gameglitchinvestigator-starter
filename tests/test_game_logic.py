from logic_utils import check_guess, get_range_for_difficulty

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert message == "🎉 Correct!"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"

def test_get_range_easy():
    low, high = get_range_for_difficulty("Easy")
    assert low == 1
    assert high == 20

def test_get_range_normal():
    low, high = get_range_for_difficulty("Normal")
    assert low == 1
    assert high == 100

def test_get_range_hard():
    low, high = get_range_for_difficulty("Hard")
    assert low == 1
    assert high == 1000

def test_get_range_invalid():
    low, high = get_range_for_difficulty("Invalid")
    assert low == 1
    assert high == 100  # defaults to Normal
