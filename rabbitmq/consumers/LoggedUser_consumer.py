import asyncio
import aio_pika
from decouple import config


RABBITMQ_URL = config('RABBITMQ_URL')


async def connect_to_rabbitmq():
    connection = await aio_pika.connect_robust(RABBITMQ_URL)
    async with connection:
        channel = await connection.channel()  # Create a channel
        queue = await channel.declare_queue('user_login_queue', durable=True)

        # Define a callback function for when a message is received
        async def on_message(message: aio_pika.IncomingMessage):
            try:
                async with message.process():
                    # Process the message
                    print(f"Received message: {message.body}")
            except Exception as e:
                print(f"Error processing message: {e}")
                await message.nack(requeue=True)

        # Start consuming messages
        await queue.consume(on_message)
        print("Consumer is running. Press CTRL+C to stop.")
        # This will block the process and keep consuming messages
        await asyncio.Future()

    # Close the connection
    await connection.close()


if __name__ == "__main__":
    asyncio.run(connect_to_rabbitmq())