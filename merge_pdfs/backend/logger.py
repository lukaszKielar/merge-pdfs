import logging
import sys
from logging.handlers import QueueHandler, QueueListener
from queue import SimpleQueue


class AppLogger:
    @classmethod
    def default(cls) -> logging.Logger:
        """Defines non-blocking application logger.
        Inspiration: https://www.zopatista.com/python/2019/05/11/asyncio-logging/

        Returns:
            logging.Logger: Root logger
        """
        # get root logger
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)

        formatter = logging.Formatter(
            fmt="%(asctime)s | %(levelname)8s | %(message)60s | %(filename)s:%(lineno)d at %(name)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )

        stdout_handler = logging.StreamHandler(stream=sys.stdout)
        stdout_handler.setLevel(logging.DEBUG)
        stdout_handler.setFormatter(formatter)

        queue = SimpleQueue()
        queue_handler = QueueHandler(queue)
        logger.addHandler(queue_handler)

        listener = QueueListener(queue, *[stdout_handler], respect_handler_level=True)

        listener.start()

        return logger
