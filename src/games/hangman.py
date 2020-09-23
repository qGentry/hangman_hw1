class Hangman:

    def __init__(self, secret_word: str, lives: int = 5):
        self.secred_word = secret_word
        self.chars = set(secret_word)
        self.guessed_chars = set()
        self.max_lives = lives
        self.cur_lives = lives

    def make_current_output(self) -> (str, bool):
        result = []
        guessed = True
        for char in self.secred_word:
            if char in self.guessed_chars:
                result.append(char)
            else:
                guessed = False
                result.append('*')
        return ''.join(result), guessed

    def try_guess(self, char: str) -> bool:
        if char in self.chars:
            self.guessed_chars.add(char)
            cur_word_state, guessed = self.make_current_output()
            print(f"Hit!\n\nThe word: {cur_word_state}\n")
            if guessed:
                print("You won!")
                return False
            return True
        cur_word_state, _ = self.make_current_output()
        self.cur_lives -= 1
        print(f"Missed, mistake {self.max_lives - self.cur_lives} out "
              f"of {self.max_lives}.\n\nThe word: {cur_word_state}\n")
        if self.cur_lives <= 0:
            print("You lost")
            return False
        return True
