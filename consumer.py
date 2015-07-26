import pika

credentials = pika.PlainCredentials('guest', 'guest')
parameters = pika.ConnectionParameters('localhost', 5672, '/', credentials)
connection = pika.BlockingConnection()

channel = connection.channel()
channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    print " [x] Recieved %r" % (body,)


channel.basic_consume(callback, queue='hello', no_ack=True)

print ' [*] Waiting for messages. To exit press CTRL+C'

channel.start_consuming()
