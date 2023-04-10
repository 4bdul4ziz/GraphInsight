from math import log10

from .preprocessor import Preprocessor
from .graph import Undirected_Graph
from .page_rank import page_rank_algorithm

def measure_similarity(sent1_words, sent2_words):
    intersection = set(sent1_words) & set(sent2_words)
    numerator = len(intersection)
    denominator = log10(len(sent1_words)) + log10(len(sent2_words))
    if (denominator == 0):
        return 0
    else:
        return numerator / denominator

def text_rank_algorithm(source_text):
    # Preprocess the source text
    preprocessor = Preprocessor(source_text)
    sentences = preprocessor.get_sentences()
    clean_words = preprocessor.get_clean_words()

    graph = Undirected_Graph()
    for sent in sentences:
        graph.add_vertex(sent)
    
    for index1 in range(len(sentences)):
        for index2 in range(len(sentences)):
            sent1 = sentences[index1]
            sent2 = sentences[index2]
            sent1_words = clean_words[index1]
            sent2_words = clean_words[index2]
            similarity = measure_similarity(sent1_words, sent2_words)
            if (similarity != 0):
                graph.add_edge(sent1, sent2, similarity)

    for sent in sentences:
        neighbours = graph.get_neighbours(sent)
        weight_sum = 0
        for (nb, weight) in neighbours:
            weight_sum += weight

        scaled_neighbours = []
        for (nb, weight) in neighbours:
            scaled_weight = weight / weight_sum
            scaled_neighbours.append((nb, scaled_weight))
        graph.set_neighbours(sent, scaled_neighbours)

    ranked_sentences = page_rank_algorithm(graph)

    final_result = []
    for (sent, prob) in ranked_sentences:
        order = sentences.index(sent)
        final_result.append((sent, prob, order))

    return final_result
