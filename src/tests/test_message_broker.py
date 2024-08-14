import unittest
from unittest.mock import MagicMock

from src.core.entities.log_entry import LogEntry
from src.infrastructure.message_broker.rabbitmq_broker import RabbitMQBroker


class TestRabbitMQBroker(unittest.TestCase):
    def test_publish(self):
        broker = RabbitMQBroker("localhost", "test_queue")
        broker.channel = MagicMock()
        log = LogEntry("2023-08-08 12:00:00", "INFO", "Test info log message")
        broker.publish(log)
        broker.channel.basic_publish.assert_called_once()


if __name__ == "__main__":
    unittest.main()
