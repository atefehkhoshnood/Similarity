# content intelligence: document classification
# Atefeh Khoshnood
# January 2020
###############################################

from collections import defaultdict
import os

from utils import *
from similarity import Similarity


def prepare_categories():
    base_path = os.path.abspath('')
    folder_path = os.path.join(base_path, 'data')
    categories = defaultdict()

    for file in os.listdir(folder_path):
        if file.endswith(".txt"):
            file_path = os.path.join(folder_path, file)
            filename, extension = parse_file_name(file)
            with open(file_path, 'r') as f:
                lines = []
                for line in f:
                    lines.append(line.replace('\n', ''))
            tokens = [token for line in lines for token in line.split()]
            tokens_no_numbers = remove_numbers(tokens)
            tokens_no_punctuations = remove_punctuations(tokens_no_numbers)
            tokens_no_stop_words = remove_stop_words(tokens_no_punctuations)

            token_frequencies = defaultdict(int)
            for token in tokens_no_stop_words:
                token_frequencies[token] += 1

            categories[filename] = token_frequencies
    return categories


def prepare_test_data():
    base_path = os.path.abspath('')
    file_path = os.path.join(base_path, 'resources/test_data.txt')
    with open(file_path, 'r') as f:
        lines = []
        for line in f:
            lines.append(line.replace('\n', ''))
    tokens = [token for line in lines for token in line.split()]
    tokens_no_numbers = remove_numbers(tokens)
    tokens_no_punctuations = remove_punctuations(tokens_no_numbers)
    tokens_no_stop_words = remove_stop_words(tokens_no_punctuations)

    token_frequencies = defaultdict(int)
    for token in tokens_no_stop_words:
        token_frequencies[token] += 1
    return token_frequencies


def main():

    cats = prepare_categories()

    test_token_freqs = prepare_test_data()

    similarity = Similarity(cats=cats, data=test_token_freqs)

    print(max(similarity.jaccard(), key=similarity.jaccard().get))
    print(max(similarity.cosine(), key=similarity.cosine().get))


if __name__ == '__main__':
    main()
