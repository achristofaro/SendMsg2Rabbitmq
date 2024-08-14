from src.core.interfaces.log_reader import LogReader
from src.core.interfaces.message_broker import MessageBroker


class ProcessLogs:
    def __init__(self, log_reader: LogReader, message_broker: MessageBroker):
        self.log_reader = log_reader
        self.message_broker = message_broker

    def execute(self):
        logs = self.log_reader.read_logs()
        for log in logs:
            try:
                self.message_broker.publish(log)
            except Exception as e:
                print(f"Failed to publish log on broker: {e}")
                raise

    def close(self):
        self.log_reader = list.clear
        self.message_broker.close()
