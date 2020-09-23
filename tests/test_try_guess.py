import unittest
from utils.make_hangman_state import make_hangman_state

TEST_CASES = [
    {
        "hangman_state": make_hangman_state("mama", 5, 5, {"m"}),
        "input": "a",
        "output": False,
    },
    {
        "hangman_state": make_hangman_state("mama", 5, 5, {"a"}),
        "input": "m",
        "output": False,
    },
    {
        "hangman_state": make_hangman_state("mama", 5, 5, set()),
        "input": "m",
        "output": True,
    },
    {
        "hangman_state": make_hangman_state("mama", 5, 5, {"m"}),
        "input": "k",
        "output": True,
    },
    {
        "hangman_state": make_hangman_state("yeild", 5, 5, {"d"}),
        "input": "y",
        "output": True,
    },
    {
        "hangman_state": make_hangman_state("yeild", 1, 5, {"d"}),
        "input": "u",
        "output": False,
    },
    {
        "hangman_state": make_hangman_state("yeild", 1, 5, {"y", "d"}),
        "input": "i",
        "output": True,
    },
    {
        "hangman_state": make_hangman_state("mama", 1, 5, {"m"}),
        "input": "u",
        "output": False,
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
