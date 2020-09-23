from games import Hangman


def make_hangman_state(
        secred_word: str,
        cur_lives: int,
        max_lives: int,
        guessed_char: set) -> Hangman:
    hangman = Hangman(secred_word, max_lives)
    hangman.cur_lives = cur_lives
    hangman.guessed_chars = guessed_char
    return hangman
