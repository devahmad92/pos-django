import json
import logging
import os
import requests
import psycopg2
from pusher_push_notifications import PushNotifications
import boto3

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

QUEUE_URL = os.getenv('QUEUE_URL')
SQS = boto3.client('sqs')

conn = psycopg2.connect(
        host=os.getenv('HOST'),
        database=os.getenv('DATABASE'),
        user=os.getenv('USER'),
        password=os.getenv('PASSWORD')
    )

beams_client = PushNotifications(
    instance_id=os.getenv('PUSH_INSTANCE_ID'),
    secret_key=os.getenv('PUSH_SECRET'),
)

cur = conn.cursor()

def consumer(event, context):
    for record in event['Records']:
        logger.info(f'Message body: {record["body"]}')
        json_data = record['body']
        data = json.loads(record['body'])
        order_id = order_id

        # Integrators
        try:
            response =  requests.post("url", json = json_data)

            if response.status_code == 200:
            # save respone to database
                cur.execute("INSERT INTO orders (order, delivery, loyalty, food_ordering) VALUES (%s, %s, %s, %s)",
                    (order_id, response.get("delivery_status"), response.get("loyalty_status"), response.get("food_ordering_status")))

                logger.info(f'integrators updated, ORDER: {order_id}')
            
            raise Exception(f"something went wrong ', response:  {response.status_code} - {response.text}")
            
        except Exception as e:
            logger.error(f'Order {order_id} - {e}')

        try:
            response = beams_client.publish_to_users(
                user_id=data.get("user_id"),
                publish_body={
                    'apns': {
                        'aps': {
                            'alert': 'Your order is on the way!'
                        }
                    },
                    'fcm': {
                        'notification': {
                            'title': 'Order Status',
                            'body': 'Yummy!'
                        }
                    }
                }
            )
            
            logger.info(f'Notificcation sent, ORDER: {order_id}, USER: {data.get("user_id")}')

        except Exception as e:
            logger.error(f'Notificcation, ORDER: {order_id}, USER: {data.get("user_id")} - {e}')







