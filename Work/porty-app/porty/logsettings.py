# This file sets up basic configuration of the logging module.
# Change settings here to adjust logging output as needed.
import logging
logging.basicConfig(
    filename='app.log',            # Name of the log file (omit to use stderr)
    filemode='w',                  # File mode (use 'a' to append)
    # Logging level (DEBUG, INFO, WARNING, ERROR, or CRITICAL)
    level=logging.DEBUG,
)
