from abc import ABC, abstractmethod
from typing import List

from src.core.entities.log_entry import LogEntry


class LogReader(ABC):
    @abstractmethod
    def read_logs(self) -> List[LogEntry]:
        raise NotImplementedError
