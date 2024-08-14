import os

from src.core.entities.log_entry import LogEntry
from src.core.interfaces.log_reader import LogReader


class FileLogReader(LogReader):
    def __init__(self, directory: str):
        self.directory = directory

    def read_logs(self) -> list[LogEntry]:
        logs = []
        for filename in os.listdir(self.directory):
            if filename.endswith(".txt"):
                with open(os.path.join(self.directory, filename), "r") as file:
                    for line in file:
                        timestamp, level, message = line.strip().split(",", 2)
                        logs.append(LogEntry(timestamp, level, message))
        return logs
