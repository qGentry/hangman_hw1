from games import Hangman
import random
import argparse


def choose_random_word(source) -> str:
    words = []
    with open(source, 'r') as f:
        for line in f:
            words.append(line.strip('\n'))
    random_word_index = random.randint(0, len(words))
    return words[random_word_index]


def main():
    parser = argparse.ArgumentParser(description='This is hangman game')
    parser.add_argument('--vocab-path', type=str, default='configs/hangman_vocab.txt',
                        help='You can specify your own vocab by passing path to it in this argument')
    args = parser.parse_args()
    hangman = Hangman(secret_word=choose_random_word(args.vocab_path))
    while True:
        print("Guess a letter:")
        cur_char = input()
        keep_playing = hangman.try_guess(cur_char)
        if not keep_playing:
            break


if __name__ == '__main__':
    main()
