from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from celery import shared_task
from chatterbot import ChatBot
from chatterbot.ext.django_chatterbot import settings

channels = get_channel_layer()


@shared_task
def get_response(channel_name, input_data):
    chatterbot = ChatBot(**settings.CHATTERBOT)
    response = chatterbot.get_response(input_data)
    response_data = response.serialize()

    async_to_sync(channels.send)(
        channel_name,
        {
            "type": "chat.message",
            "text": {"msg": response_data["text"], "source": "bot"},

        },

    )
