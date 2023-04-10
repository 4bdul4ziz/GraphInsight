from math import ceil
from .text_rank import text_rank_algorithm

class Summarizer:
    def __init__(self, text):
        self.text = text

    def rank_sentences(self):
        if (hasattr(self, "ranked_sentences")):
            return self.ranked_sentences
        self.ranked_sentences = text_rank_algorithm(self.text)
        return self.ranked_sentences

    def summarize(self, summarization_ratio = 0.3):
        ranked_sentences = self.rank_sentences()
        num_sent_in_summary = ceil(summarization_ratio * len(ranked_sentences))
        unordered_summary = ranked_sentences[:num_sent_in_summary]
        ordered_summary_dict = sorted(unordered_summary, key = lambda item: item[2])
        ordered_summary_list = [sent for (sent, prob, order) in ordered_summary_dict]
        return "\n".join(ordered_summary_list)
