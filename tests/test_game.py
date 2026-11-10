
import pytest
from nyu_wordle.game import WordleGame


def test_initial_game_state():
    game = WordleGame("apple")

    assert game.get_status() == "ongoing"
    assert game.get_remaining_attempts() == 6
    assert game.get_guess_history() == []


def test_tracking_attempts():
    game = WordleGame("apple", max_attempts=4)

    assert game.get_remaining_attempts() == 4

    game.submit_guess("grape")
    assert game.get_remaining_attempts() == 3

    game.submit_guess("melon")
    assert game.get_remaining_attempts() == 2
    assert game.get_guess_history() == ["grape", "melon"]


def test_win_condition():
    game = WordleGame("apple")

    assert game.submit_guess("apple") == "won"
    assert game.get_status() == "won"
    assert game.get_remaining_attempts() == 5

    with pytest.raises(ValueError):
        game.submit_guess("grape")


def test_loss_condition():
    game = WordleGame("apple", max_attempts=2)

    assert game.submit_guess("grape") == "ongoing"
    assert game.submit_guess("melon") == "lost"
    assert game.get_remaining_attempts() == 0

    with pytest.raises(ValueError):
        game.submit_guess("apple")


def test_win_on_final_attempt():
    game = WordleGame("apple", max_attempts=2)

    game.submit_guess("grape")

    assert game.submit_guess("apple") == "won"
    assert game.get_status() == "won"


def test_invalid_guess():
    game = WordleGame("apple")

    with pytest.raises(ValueError):
        game.submit_guess("cat")

    with pytest.raises(ValueError):
        game.submit_guess(123)

    assert game.get_remaining_attempts() == 6
    assert game.get_status() == "ongoing"


def test_reset_game():
    game = WordleGame("apple", max_attempts=3)

    game.submit_guess("apple")
    assert game.get_status() == "won"

    game.reset_game("grape")

    assert game.get_status() == "ongoing"
    assert game.get_remaining_attempts() == 3
    assert game.get_guess_history() == []
    assert game.secret_word == "grape"


def test_invalid_configuration():
    with pytest.raises(ValueError):
        WordleGame("", 6)

    with pytest.raises(ValueError):
        WordleGame("apple", 0)

    with pytest.raises(ValueError):
        WordleGame("apple", -1)
