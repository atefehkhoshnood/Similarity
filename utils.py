# content intelligence: document classification
# Atefeh Khoshnood
# January 2020
###############################################

import os


def parse_file_name(filename):
    filename_no_extension = filename.split('.')[0]
    extension = filename.split('.')[1]
    return filename_no_extension , extension


def remove_numbers(tokens):
    tokens_no_number = []
    for token in tokens:
        t = ''
        for char in token:
            if not char.isdigit():
                t += char
        if t:
            tokens_no_number.append(t)
    return tokens_no_number


def remove_punctuations(tokens):
    """
    :param tokens: list(str)
    :return: list(str)
    """
    punctuations = ['"', "'", '-', ',', '.', ':', ';', '?', '!', ']', '[', ')', '(']
    tokens_no_punctuations = []
    for token in tokens:
        t = ''
        for char in token:
            if char not in punctuations:
                t += char
        if t:
            tokens_no_punctuations.append(t)
    return tokens_no_punctuations


def remove_stop_words(tokens):
    """
    :param tokens: list(str)
    :return: list(str)
    """
    base_path = os.path.abspath('')
    file_path = os.path.join(base_path, 'resources/stop_words.txt')
    with open(file_path, 'r') as file:
        stop_words = [word.replace('\n', '') for word in file]
    tokens_no_stop_words = [token.lower() for token in tokens if token.lower() not in stop_words]
    return tokens_no_stop_words
