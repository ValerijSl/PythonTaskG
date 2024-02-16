import logging

def setup_logging(log_file='app.log', level=logging.INFO):
    """Set up the logging configuration."""
    logging.basicConfig(
        filename=log_file,
        filemode='a',
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        level=level
    )
    # Adding handler for console output
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)
    formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    console_handler.setFormatter(formatter)
    logging.getLogger('').addHandler(console_handler)