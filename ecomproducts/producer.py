import pika, json

params = pika.URLParameters('amqps://pxlurbdq:8WnK7NvNTXz6mQzrvUe3hRaDoSa2cMmv@hawk.rmq.cloudamqp.com/pxlurbdq')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, product_id, quantity, price):
    properties = pika.BasicProperties(method)
    body = json.dumps({'id': product_id, 'quantity': quantity, 'price': price})
    channel.basic_publish(exchange='', routing_key='cart', body=body, properties=properties)
