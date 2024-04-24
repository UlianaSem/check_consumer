import json
import logging

from confluent_kafka import Consumer

from django.conf import settings
from django.core.management import BaseCommand

from main import models


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class Command(BaseCommand):

    def handle(self, *args, **options):
        config = {
            'bootstrap.servers': f'{settings.KAFKA_HOST}:9092',
            'client.id': settings.KAFKA_CLIENT,
            'group.id': settings.KAFKA_CLIENT,
            'auto.offset.reset': settings.KAFKA_RESET
        }

        consumer = Consumer(config)
        topic = "check_data"
        consumer.subscribe([topic])

        try:
            while True:
                msg = consumer.poll(1.0)
                if msg is None:
                    continue
                elif msg.error():
                    continue
                else:
                    check_dict = json.loads(msg.value().decode('utf-8'))
                    models.Check.objects.create(
                        check_json=check_dict
                    )
                    logger.info(f'Create check {check_dict.get("transaction_id")}')

        except KeyboardInterrupt:
            pass
        finally:
            consumer.close()
