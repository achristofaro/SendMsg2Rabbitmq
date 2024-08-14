import pika
import pika.exceptions

from src.core.entities.log_entry import LogEntry
from src.core.interfaces.message_broker import MessageBroker


class RabbitMQBroker(MessageBroker):
    def __init__(self, host: str, queue: str):
        self.host = host
        self.queue = queue
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=self.host)
        )
        self.channel = self.connection.channel()
        self.channel.queue_declare(
            queue=self.queue, durable=True, passive=True
        )  # Passive=True -> RabbitMQ não criará a fila se ela não existir
        self.channel.confirm_delivery()  # Ativa o modo de confirmação de entrega no channel
        print(f"Open connection with RabbitMQ host: {self.host}")

    def publish(self, log: LogEntry):
        try:
            self.channel.basic_publish(
                exchange="",
                routing_key=self.queue,
                body=f"{log.timestamp},{log.level},{log.message}",
                properties=pika.BasicProperties(
                    delivery_mode=2,  # Tornar a mensagem persistente
                ),
            )
            print(
                f"Successfully published log: {log.timestamp},{log.level},{log.message}"
            )
        except pika.exceptions.AMQPError as e:
            print(f"Failed to publish message to RabbitMQ: {e}")
            raise

    def close(self):
        self.connection.close()
        print(f"Close connection with RabbitMQ host: {self.host}")
