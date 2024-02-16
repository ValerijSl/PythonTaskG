import pandas as pd
import re
from .logger import setup_logging
import logging

class DataPreprocessor:
    def __init__(self):
        pass

    def clean_phrases(self, csv_path, clean_csv_path='data/cleaned_phrases.csv'):
        # Configure logging
        setup_logging()

        # Get the logger for the current script
        logger = logging.getLogger(__name__)

        
        phrases = pd.read_csv(csv_path)
        phrases.dropna(inplace=True)
        phrases['Phrases'] = phrases['Phrases'].str.strip()
        phrases['Phrases'] = phrases['Phrases'].apply(lambda x: re.sub(r"[^\w\s?]", '', x))
        #Also need to get rid of czech phrases, vectors have eng only
        phrases.to_csv(clean_csv_path, index=False)
        phrases['Phrases'].tolist()
        return phrases