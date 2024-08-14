from src.core.use_cases.process_logs import ProcessLogs
from src.infrastructure.log_reader.file_log_reader import FileLogReader
from src.infrastructure.message_broker.rabbitmq_broker import RabbitMQBroker

from .config import Config


def get_process_logs_use_case():
    log_reader = FileLogReader(Config.LOG_DIRECTORY)
    message_broker = RabbitMQBroker(Config.RABBITMQ_HOST, Config.RABBITMQ_QUEUE)
    return ProcessLogs(log_reader, message_broker)
