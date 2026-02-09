#!/usr/bin/env python
import os
import sys

import pika


def callback(ch, method, properties, body):
    print(f" [x] Received {body}")


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    channel = connection.channel()

    channel.queue_declare("hello")

    channel.basic_consume(queue="hello", auto_ack=True, on_message_callback=callback)

    print(" [*] Waiting for messages. To exit press CTRL+C")
    channel.start_consuming()


if __name__ == "__main__":
    try:
        main()
    except:
        print("Interrupted")
        try:
            sys.exit(0)
        except:
            os._exit(0)
