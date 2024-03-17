import pika

credentials = pika.PlainCredentials('guest','guest')
parameters = pika.ConnectionParameters('localhost', 5672,"/",credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.queue_declare(queue='checking-student')

def on_message(channel, method_frame, header_frame, body):
    print(method_frame.delivery_tag)
    print(body)
    print()
    channel.basic_ack(delivery_tag=method_frame.delivery_tag)


if __name__ == '__main__':
    try:
        channel.basic_consume(queue='checking-student',on_message_callback=on_message)
        channel.start_consuming()
    except KeyboardInterrupt:
        channel.stop_consuming()
    connection.close()
