# ecomms
This is a simple micro service example that uses RabbitMQ and 2 django projects
* products django project produces
* carts django project consumes

# Steps to run it
* Open both projects in seperate windows or pycharm projects
* run the migrate command
* create a super user for both apps
* open admin on products project and add some products
* create account on cloudamqp.com
* watch the RabbitMQ section of this vieo https://www.youtube.com/watch?v=0iB5IPoTDts and add the url in products producer.py and carts consumer.py
* run the producer and consumer
* run both the servers
* send 127.0.0.1:8000/api/products/1/add with a POST request with form date {quantity: 2} from the products django project
* Observer that a new item was added to the carts django project
