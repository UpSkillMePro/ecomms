import pika, json, os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ecomcarts.settings")
django.setup()

from carts.models import Cart, Items

params = pika.URLParameters('amqps://pxlurbdq:8WnK7NvNTXz6mQzrvUe3hRaDoSa2cMmv@hawk.rmq.cloudamqp.com/pxlurbdq')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='cart')

Cart.objects.create(title="My Cart", user=1).save()


def callback(ch, method, properties, body):
    print('Received in Cart')
    data = json.loads(body)
    print(data)

    if properties.content_type == 'product_added_to_cart':
        Items.objects.create(product=data['id'], quantity=data['quantity'], price=data['price'],
                             cart=Cart.objects.get(title="My Cart")).save()
        print('Item added to cart')


channel.basic_consume(queue='cart', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()
