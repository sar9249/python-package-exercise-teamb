from nyu_wordle.check_guess import check_guess


def test_all_correct():
    assert check_guess("apple", "apple") == [
        "correct", "correct", "correct", "correct", "correct"
    ]


def test_some_correct_and_present():
    assert check_guess("plate", "plant") == [
        "correct", "correct", "correct", "present", "absent"
    ]


def test_all_absent():
    assert check_guess("zzzzz", "apple") == [
        "absent", "absent", "absent", "absent", "absent"
    ]


def test_case_insensitive():
    assert check_guess("APPLE", "apple") == [
        "correct", "correct", "correct", "correct", "correct"
    ]


def test_repeated_letters():
    assert check_guess("allee", "apple") == [
        "correct", "present", "absent", "absent", "correct"
    ]


def test_repeated_letters_extra():
    assert check_guess("speed", "pearl") == [
        "absent", "present", "present", "absent", "absent"
    ]


def test_all_present():
    assert check_guess("pleap", "apple") == [
        "present", "present", "present", "present", "present"
    ]


def test_single_letter():
    assert check_guess("a", "a") == ["correct"]


def test_uppercase_word():
    assert check_guess("apple", "APPLE") == [
        "correct", "correct", "correct", "correct", "correct"
    ]
