import pika
from models import Contact
import faker


def generate_data_list():
    fake = faker.Faker()
    contacts = []
    for i in range(10):
        contacts.append({'name': fake.name(), 'email': fake.email(), 'isSent': False})
    return contacts


def seed_models(model, seeds):
    for seed in seeds:
        model(**seed).save()


def broker_connection():
    credentials = pika.PlainCredentials('guest', 'guest')
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))

    return connection


def broker_chanel(connection):
    channel = connection.channel()
    channel.queue_declare(queue='email_queue')
    return channel


def broker_send_message(channel, body):
    channel.basic_publish(exchange='', routing_key='email_queue', body=str(body))


def main():
    seed_models(Contact, generate_data_list())
    contacts = Contact.objects()
    connection = broker_connection()

    for contact in contacts:
        body_message = contact.id
        broker_send_message(broker_chanel(connection), body_message)

    connection.close()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
