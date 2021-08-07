from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core import serializers


import boto3

from .models import Order

@receiver(post_save, sender=Order)
def my_handler(sender, **kwargs):
    # Sending data to sqs

    # sqs = boto3.client('sqs')

    # queue_url = 'SQS_QUEUE_URL'

    # serialized_obj = serializers.serialize('json', [ sender, ])


    # # Send message to SQS queue
    # response = sqs.send_message(
    #     QueueUrl=queue_url,
    #     DelaySeconds=10,
    #     MessageAttributes=serialized_obj
    # )
    pass