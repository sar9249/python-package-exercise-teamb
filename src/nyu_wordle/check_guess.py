def check_guess(guess, word):
    """
    Compare a guess to the target word.

    Assumes the guess has already been validated.

    Returns a list of feedback for each letter:
    - "correct": right letter, right position
    - "present": right letter, wrong position
    - "absent": letter not available in the word
    """

    guess = guess.lower()
    word = word.lower()

    result = ["absent"] * len(guess)
    remaining = {}

    # First pass: mark letters in the correct position
    for i in range(len(guess)):
        if guess[i] == word[i]:
            result[i] = "correct"
        else:
            letter = word[i]
            remaining[letter] = remaining.get(letter, 0) + 1

    # Second pass: mark letters in the wrong position
    for i in range(len(guess)):
        if result[i] == "correct":
            continue

        letter = guess[i]

        if remaining.get(letter, 0) > 0:
            result[i] = "present"
            remaining[letter] -= 1

    return result
