import random
import argparse

from games import Hangman


def choose_random_word(source) -> str:
    words = []
    with open(source, 'r') as file:
        for line in file:
            words.append(line.strip('\n'))
    random_word_index = random.randint(0, len(words) - 1)
    return words[random_word_index]


def main():
    parser = argparse.ArgumentParser(description='This is hangman game')
    parser.add_argument('--vocab-path', type=str, default='configs/hangman_vocab.txt',
                        help='You can specify your own vocab by passing it path in this argument')
    args = parser.parse_args()
    hangman = Hangman(secret_word=choose_random_word(args.vocab_path))
    while True:
        print("Guess a letter:")
        cur_char = input()
        keep_playing, output = hangman.try_guess(cur_char)
        print(output)
        if not keep_playing:
            break


if __name__ == '__main__':
    main()
