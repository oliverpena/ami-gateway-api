import atexit
from logging.handlers import QueueHandler, QueueListener
from queue import Queue
from typing import List


class LoggingQueueListenerHandler(QueueHandler):
    """
    This is the blueprint of a Queue Listener Log Handler.
    it provides a way of queueing log events to be passed
    to logging handlers and be processed by a separate
    thread, providing a non-blocking way of logging.
    """

    def __init__(self, handlers: List, auto_run=True, queue=Queue(-1)) -> None:
        """
        Create a new instance of the log records queue listener and
        the queue itself.

        param: List of logging Handlers: handlers. Logging handlers
        to be used when a log records needs to be processed.

        param: boolean auto_run: boolean flag to initiate the listener
        thread automaticaly.

        param: Queue queue: Queue object that queues the log records.
        """
        self._queue = queue
        self._handlers = handlers
        super().__init__(self._queue)
        self._listener = QueueListener(self._queue, self._handlers)
        if auto_run:
            self._start()
            atexit.register(self._stop)

    def _start(self):
        """
        Method to initiate the listener thread of the queue of log records.
        """
        self._listener.start()

    def _stop(self):
        """
        Method to stop the listener thread of the queue of log records.
        """
        self._listener.stop()

    def emit(self, record):
        """
        Method to dispatch log records to be logged.
        """
        return super().emit(record)
