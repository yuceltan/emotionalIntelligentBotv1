import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from channels.layers import get_channel_layer
from chatterbot import ChatBot
from chatterbot.ext.django_chatterbot import settings

channels = get_channel_layer()

class UserConsumer(WebsocketConsumer):
    def receive(self, text_data=None, **kwargs):
        text_data_json = json.loads(text_data)

        async_to_sync(self.channel_layer.send)(
            self.channel_name,
            {
                "type": "chat_message",
                "text": {"msg": text_data_json["text"], "source": "user"},
            },
        )

        # Call the get_response function to execute the code for getting a response from the chatbot
        self.get_response(self.channel_name, text_data_json["text"])

    # Define the get_response function at the class level
    def get_response(self, channel_name, input_data):
        chatterbot = ChatBot(**settings.CHATTERBOT)
        response = chatterbot.get_response(input_data)
        response_data = response.serialize()

        async_to_sync(channels.send)(
            channel_name,
            {
                "type": "chat_message",
                "text": {"msg": response_data["text"], "source": "bot"},
            },
        )

    def chat_message(self, event):
        text = event["text"]
        self.send(text_data=json.dumps({"text": text}))