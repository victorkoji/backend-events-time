import logging


class Logger(logging.Logger):
    def __init__(self, name, level=logging.INFO):
        super().__init__(name, level)

        formatter = logging.Formatter(
            '%(levelname)-9s %(asctime)s | %(name)s | %(message)s',
            '%Y-%m-%d %H:%M:%S.%03d'
        )
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)
        self.addHandler(handler)
