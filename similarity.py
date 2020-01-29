# content intelligence: document classification
# Atefeh Khoshnood
# January 2020
###############################################

from collections import defaultdict
import numpy as np


class SimilarityError(Exception):
    pass


class Similarity:
    def __init__(self, cats, data):
        self.cats = cats
        self.data = data
        self.word_dictionary = set()
        self.build_word_dictionary()

    def build_word_dictionary(self):
        for _, word_freq in self.cats.items():
            for word, _ in word_freq.items():
                self.word_dictionary.add(word)
        for word, _ in self.data.items():
            self.word_dictionary.add(word)

    def jaccard(self):
        cats = []
        for cat, word_freq in self.cats.items():
            x = []
            for word, freq in word_freq.items():
                x.append(word)
            cats.append((cat, x))

        y = [k for k,v in self.data.items()]

        result = defaultdict(float)
        for cat in cats:
            label, x = cat
            intersection_cardinality = len(set.intersection(*[set(x), set(y)]))
            union_cardinality = len(set.union(*[set(x), set(y)]))
            result[label] = intersection_cardinality / float(union_cardinality)

        return result

    @staticmethod
    def total_words(word_freq):
        count = 0
        for _, freq in word_freq.items():
            count += freq
        return count

    def compute_tf(self, word_freq):
        word_tf = defaultdict(float)
        count = self.total_words(word_freq)
        for word, freq in word_freq.items():
            word_tf[word] = freq/count
        return word_tf

    def text_vector(self, word_tf):
        word_dictionary = list(self.word_dictionary)
        v = np.zeros(len(word_dictionary), dtype=float)

        for index, word in enumerate(word_dictionary):
            if word_tf[word]:
                v[index] = word_tf[word]
        return v

    def cosine(self):
        result = defaultdict(float)

        word_tf_data = self.compute_tf(self.data)
        v_data = self.text_vector(word_tf_data)
        for cat, word_freq in self.cats.items():
            word_tf_cat = self.compute_tf(word_freq)
            v_cat = self.text_vector(word_tf_cat)
            result[cat] = np.dot(v_cat, v_data) / (np.sqrt(np.dot(v_data, v_data)) * np.sqrt(np.dot(v_cat, v_cat)))

        return result
