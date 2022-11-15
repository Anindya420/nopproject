import logging
class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename="C:\\Users\hp\\PycharmProjects\\nopproject\\logs\\automation.log")
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
