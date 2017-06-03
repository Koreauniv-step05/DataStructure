# Timer
import time
# Logger
import logging


class Timer():
    __instance = None

    @classmethod
    def __getInstance(cls):
        return cls.__instance

    @classmethod
    def getInstance(cls, *args, **kargs):
        cls.__instance = cls(*args, **kargs)
        cls.instance = cls.__getInstance
        return cls.__instance

    def tic(self):
        self.start_time = time.time()

    def toc(self):
        return time.time() - self.start_time

    def toc_in_millis(self):
        return self.toc()*1000

class Logger():
    __instance = None

    @classmethod
    def __getInstance(cls):
        return cls.__instance

    @classmethod
    def getInstance(cls, *args, **kargs):
        cls.__instance = cls(*args, **kargs)
        cls.instance = cls.__getInstance
        return cls.__instance

    @classmethod
    def getLogger(cls, log_level):
        logger = cls.getInstance().logger
        if log_level is "DEBUG":
            logger.setLevel(logging.DEBUG)
        elif log_level is "INFO":
            logger.setLevel(logging.INFO)
        return logger

    def __init__(self):
        self.logger = logging.getLogger("JYP")
        self.formatter = \
            logging.Formatter('[%(levelname)s|%(filename)s:%(lineno)s] '
                              '%(asctime)s > %(message)s')
        self.streamHandler = logging.StreamHandler()
        self.streamHandler.setFormatter(self.formatter)

        self.logger.addHandler(self.streamHandler)

