import pika
import json
from decouple import config

RABBITMQ_HOST = config('RABBITMQ_HOST')
RABBITMQ_PORT = config('RABBITMQ_PORT')
RABBITMQ_USER = config('RABBITMQ_USER')
RABBITMQ_PASSWORD = config('RABBITMQ_PASSWORD')


def create_connection():
    credentials = pika.PlainCredentials(RABBITMQ_USER, RABBITMQ_PASSWORD)
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        host=RABBITMQ_HOST,
        port=RABBITMQ_PORT,
        credentials=credentials
    ))
    return connection
