import unittest
from games.utils.make_hangman_state import make_hangman_state

TEST_CASES = [
    {
        "hangman_state": make_hangman_state("mama", 5, 5, {"m"}),
        "output": ("m*m*", False),
    },
    {
        "hangman_state": make_hangman_state("mama", 5, 5, {"a"}),
        "output": ("*a*a", False),
    },
    {
        "hangman_state": make_hangman_state("mama", 5, 5, {"m", "a"}),
        "output": ("mama", True),
    },
    {
        "hangman_state": make_hangman_state("mama", 5, 5, set()),
        "output": ("****", False),
    },
    {
        "hangman_state": make_hangman_state("yeild", 5, 5, set()),
        "output": ("*****", False),
    },
    {
        "hangman_state": make_hangman_state("yeild", 5, 5, {"y", "i", "l", "d"}),
        "output": ("y*ild", False),
    },
    {
        "hangman_state": make_hangman_state("yeild", 5, 5, {"y", "i", "d"}),
        "output": ("y*i*d", False),
    },
    {
        "hangman_state": make_hangman_state("yeild", 5, 5, {"d"}),
        "output": ("****d", False),
    },
    {
        "hangman_state": make_hangman_state("yeild", 5, 5, {"y", "i", "e", "l", "d"}),
        "output": ("yeild", True),
    },
]


class MyTestCase(unittest.TestCase):
    def test_make_current_output(self):
        for test in TEST_CASES:
            with self.subTest():
                hangman_output = test['hangman_state'].make_current_output()
                self.assertEqual(hangman_output, test['output'])


if __name__ == '__main__':
    unittest.main()
