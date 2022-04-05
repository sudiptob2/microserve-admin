import json
import os

import pika

RABBIT_ENDPOINT = os.environ['RABBIT_ENDPOINT']

params = pika.URLParameters(RABBIT_ENDPOINT)

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)
