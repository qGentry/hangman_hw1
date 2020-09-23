import unittest

from bin.run_hangman import choose_random_word

source = 'configs/hangman_vocab.txt'


class MyTestCase(unittest.TestCase):
    def test_choose_random_word(self):
        words = set()
        with open(source, 'r') as file:
            for line in file:
                words.add(line.strip('\n'))
        for test in range(1000):
            with self.subTest():
                random_word = choose_random_word(source)
                self.assertIn(random_word, words)


if __name__ == '__main__':
    unittest.main()
