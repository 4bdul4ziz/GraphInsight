import string
import nltk
from nltk import sent_tokenize
from nltk import word_tokenize
from nltk.corpus import stopwords


nltk.download('stopwords')

class Preprocessor:
    def __init__(self, original_text):
        self.original_text = original_text

    def get_sentences(self):
        if (hasattr(self, "sentences")):
            return self.sentences
        self.sentences = sent_tokenize(self.original_text)
        return self.sentences

    def get_words(self):
        if (hasattr(self, "words")):
            return self.words
        sentences = self.get_sentences()
        self.words = [word_tokenize(sen) for sen in sentences]
        return self.words

    def get_english_stopwords(self):
        if (hasattr(self, "english_stopwords")):
            return self.english_stopwords
        self.english_stopwords = stopwords.words("english")
        return self.english_stopwords

    def get_english_punctuations(self):
        if (hasattr(self, "punctuations")):
            return self.punctuations
        self.punctuations = list(string.punctuation)
        return self.punctuations
    
    def get_clean_words(self):
        if (hasattr(self, "clean_words")):
            return self.clean_words

        words_lol = self.get_words()
        stopwords = self.get_english_stopwords()
        punctuations = self.get_english_punctuations()

        new_words_lol = []
        for words_list in words_lol:
            new_words_list = []
            for word in words_list:
                lower = word.lower()
                if lower not in stopwords and lower not in punctuations:
                    new_words_list.append(lower)
            new_words_lol.append(new_words_list)
        
        self.clean_words = new_words_lol
        return self.clean_words
