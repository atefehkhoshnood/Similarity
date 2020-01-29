from utils import *


def test_parse_file_name():
    filename, extension = parse_file_name('test.pdf')
    assert filename == 'test' and extension == 'pdf'


def test_remove_stop_words():
    tokens = ['You', 'were', 'very', 'Well!']
    tokens_no_stop_words = remove_stop_words(tokens)
    assert tokens_no_stop_words == ['Well!']


def test_remove_numbers():
    tokens = ['data.[12]', '1990', 'July-2-2020']
    tokens_no_numbers = remove_numbers(tokens)
    assert tokens_no_numbers == ['data.[]', 'July--']


def test_remove_punctuationss():
    tokens = ['this[2]', 'is,', 'by(2)', 'all', 'means:', 'a', 'test!']
    tokens_no_punctuations = remove_punctuations(tokens)
    assert tokens_no_punctuations == ['this2', 'is', 'by2', 'all', 'means', 'a', 'test']


def test_clean_text():
    tokens = ['You!', 'were,', '100', 'percent,', 'very', 'Well:)']
    tokens_no_numbers = remove_numbers(tokens)
    tokens_no_punctuations = remove_punctuations(tokens_no_numbers)
    tokens_no_stop_words = remove_stop_words(tokens_no_punctuations)

    assert tokens_no_stop_words == ['percent']
