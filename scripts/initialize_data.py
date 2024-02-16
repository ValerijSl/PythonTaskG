import os
import gdown
from gensim.models import KeyedVectors
from logger import setup_logging
import logging

def main():
    # Configure logging
    setup_logging()

    # Get the logger for the current script
    logger = logging.getLogger(__name__)

    # Example log messages
    logger.info('Checking if the vectors CSV file exists...')
    # Check if the vectors CSV file already exists
    vectors_csv_path = 'data/vectors.csv'

    if not os.path.exists(vectors_csv_path):
        # If the binary file is not present, download it first
        model_location = 'data/GoogleNews-vectors-negative300.bin.gz'
    
        # Check if the binary file exists
        logger.info('Vectors.csv not found, checking for vectors bin...')
        if not os.path.exists(model_location):
            url = 'https://drive.google.com/uc?id=0B7XkCwpI5KDYNlNUTTlSS21pQmM'
            output = 'data/GoogleNews-vectors-negative300.bin.gz'
            gdown.download(url, output, quiet=False)
        # Load the model
        logger.info('Loading the model...')
        wv = KeyedVectors.load_word2vec_format(model_location, binary=True, limit=1000000)

        # Save the vectors in Word2Vec format as a CSV file
        wv.save_word2vec_format(vectors_csv_path)
        logger.info('Model loaded...')
    else:
        logger.info(f"'{vectors_csv_path}' already exists.")
if __name__ == "__main__":
    main()