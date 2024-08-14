from abc import ABC, abstractmethod

from src.core.entities.log_entry import LogEntry


class MessageBroker(ABC):
    @abstractmethod
    def publish(self, log: LogEntry):
        raise NotImplementedError

    def close(self):
        raise NotImplementedError
