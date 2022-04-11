import json
import os
import time

import django
import pika

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.settings")
django.setup()

from products.models import Product

RABBIT_ENDPOINT = os.environ['RABBIT_ENDPOINT']


def callback(ch, method, properties, body):
    print('Received in admin')
    product_id = json.loads(body)
    product = Product.objects.filter(
        id=product_id,
    ).first()
    if product:
        product.likes = product.likes + 1
        product.save()
        print('Product likes increased!')


class Consumer:
    """Implement the consumer script."""

    def start(self, connection):
        # if not self.connection or self.connection.is_closed:
        #     self.connection = pika.BlockingConnection(self.params)
        channel = connection.channel()
        channel.queue_declare(queue='admin')
        channel.basic_consume(
            queue='admin',
            on_message_callback=callback,
            auto_ack=True,
        )
        print('Started Consuming in admin...')
        channel.start_consuming()
        channel.close()


print('Starting the Queue.....')
consumer = Consumer()
params = pika.URLParameters(RABBIT_ENDPOINT)
while True:
    try:
        connection = pika.BlockingConnection(params)
    except:
        print('could not connect to the host. retrying in 1 sec...')
        time.sleep(1)
        continue
    consumer.start(connection)
