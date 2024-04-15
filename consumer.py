import pika

from models import Contact


def send_email(body):
    print('email was sent to ' + Contact.objects(id=body.decode()).first().name)
    Contact.objects(id=body.decode()).update_one(set__isSent=True)


def main():
    credentials = pika.PlainCredentials('guest', 'guest')
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
    channel = connection.channel()

    channel.queue_declare(queue='email_queue')

    def callback(ch, method, properties, body):
        send_email(body)

    channel.basic_consume(queue='email_queue', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

    # connection.close()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
