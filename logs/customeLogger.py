import logging
import os

class LoggGen:

    @staticmethod
    def Logger():
        # 1. Correct indentation so everything lives inside the method
        folder = "logs"

        if not os.path.exists(folder):
            os.makedirs(folder)

        logging.basicConfig(
            filename=f"{folder}\\automation.log",
           #%(levelname)s (e.g., INFO, WARNING, ERROR, CRITICAL, DEBUG)
            #%(message)s ("Login successful")).
            format="%(asctime)s : %(levelname)s : %(message)s",
            datefmt='%Y-%m-%d %H:%M:%S',
            force=True # Prevents conflicts if called multiple times
        )

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        
        # 3. Must return the logger object so your tests can use it!
        return logger
