from gensim.models import KeyedVectors
import numpy as np

class VectorAssigner:
    def __init__(self, model):
        self.model = model

    def assign_vectors(self, phrases):
        phrase_embeddings = {}
        for phrase in phrases['Phrases'].values:
            phrase_embeddings[phrase] = self.get_phrase_embedding(phrase)
        return phrase_embeddings

    def get_phrase_embedding(self, phrase):
        words = phrase.split()
        word_vectors = [self.model[word] for word in words if word in self.model]
        if not word_vectors:
            return np.zeros(self.model.vector_size)
        phrase_embedding = np.mean(word_vectors, axis=0)
        return phrase_embedding   