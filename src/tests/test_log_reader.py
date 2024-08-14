import unittest

from src.core.entities.log_entry import LogEntry
from src.infrastructure.log_reader.file_log_reader import FileLogReader


class TestFileLogReader(unittest.TestCase):
    def test_read_logs(self):
        reader = FileLogReader("./src/tests/logs/")
        logs = reader.read_logs()
        self.assertIsInstance(logs, list)
        self.assertIsInstance(logs[0], LogEntry)


if __name__ == "__main__":
    unittest.main()
