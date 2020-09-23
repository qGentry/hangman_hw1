import unittest
from games.utils.make_hangman_state import make_hangman_state

TEST_CASES = [
    {
        "hangman_state": make_hangman_state("mama", 5, 5, {"m"}),
        "input": "a",
        "output": (False, 'Hit!\n\nThe word: mama\n\nYou won!'),
    },
    {
        "hangman_state": make_hangman_state("mama", 5, 5, {"a"}),
        "input": "m",
        "output": (False, 'Hit!\n\nThe word: mama\n\nYou won!'),
    },
    {
        "hangman_state": make_hangman_state("mama", 5, 5, set()),
        "input": "m",
        "output": (True, 'Hit!\n\nThe word: m*m*\n'),
    },
    {
        "hangman_state": make_hangman_state("mama", 5, 5, {"m"}),
        "input": "k",
        "output": (True, 'Missed, mistake 1 out of 5.\n\nThe word: m*m*\n'),
    },
    {
        "hangman_state": make_hangman_state("yeild", 5, 5, {"d"}),
        "input": "y",
        "output": (True, 'Hit!\n\nThe word: y***d\n'),
    },
    {
        "hangman_state": make_hangman_state("yeild", 1, 5, {"d"}),
        "input": "u",
        "output": (False, 'Missed, mistake 5 out of 5.\n\nThe word: ****d\n\nYou lost'),
    },
    {
        "hangman_state": make_hangman_state("yeild", 1, 5, {"y", "d"}),
        "input": "i",
        "output": (True, 'Hit!\n\nThe word: y*i*d\n'),
    },
    {
        "hangman_state": make_hangman_state("mama", 1, 5, {"m"}),
        "input": "u",
        "output": (False, 'Missed, mistake 5 out of 5.\n\nThe word: m*m*\n\nYou lost'),
    },
]


class MyTestCase(unittest.TestCase):
    def test_try_guess(self):
        for test in TEST_CASES:
            with self.subTest():
                hangman_output = test['hangman_state'].try_guess(test['input'])
                self.assertEqual(hangman_output, test['output'])


if __name__ == '__main__':
    unittest.main()
