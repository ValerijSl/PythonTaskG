from .data_initializer import DataInitializer
from .preprocessor import DataPreprocessor
from .vector_assigner import VectorAssigner
from .distance_calculator import DistanceCalculator
from .phrase_matcher import PhraseMatcher
from .logger import setup_logging
import logging

def main():

    # Initialize data
    DataInit = DataInitializer()
    model = DataInit.initialize_data()

    # init DataPreprocessor and clean data
    preprocessor = DataPreprocessor()
    cleaned_data = preprocessor.clean_phrases('data/phrases.csv')
     
    vector_assigner = VectorAssigner(model)
    phrase_vectors = vector_assigner.assign_vectors(cleaned_data)

    # init DistanceCalculator and calculate distances
    distance_calculator = DistanceCalculator(phrase_vectors)
    distances = distance_calculator.calculate_distance()

    # init PhraseMatcher and find closest matches
    phrase_matcher = PhraseMatcher(cleaned_data, phrase_vectors)
    input_phrase = "Test phrase."
    closest_match = phrase_matcher.find_closest_match(input_phrase)

    # Do something with the closest match
    #print(f"The closest match to '{input_phrase}' is '{closest_match}'.")

if __name__ == "__main__":
    main()
