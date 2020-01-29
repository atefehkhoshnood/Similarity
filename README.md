# Similarity
One approach to classify documents is to measure their similarity with respect to some reference documents for each class or category.
Here, I have implemented two common similarity measures: (i) Jaccard similarity and (ii) Cosine similarity.

Reference corpus includes main part of the article from wikipedia page for mouse, cat, mousepad and computer mouse (called cmouse), under `data/` directory.

`main.py` can be run to get the class/category for any piece of text in `resources/test_data.txt`. Currently, it contains a document related to mouse, and both Jaccard and cosine similarity correctly return the class.