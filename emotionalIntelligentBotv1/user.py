import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

import emotionalIntelligentBotv1


class UserConsumer(WebsocketConsumer):
    def receive(self, text_data, bytes_data):
        json_text= json.loads(text_data)
        async_to_sync(self.channel_layer.send)(
            self.channel_name,{
                "type": "chat_message",
                "text": {"msg": json_text["text"],"source":"user" },

            },
        )
        async_to_sync(self.channel_layer.send)(
            self.channel_name,{
                "type": emotionalIntelligentBotv1.message,
                "text":{"msg":"Bot says hello","source":"bot"},

            },
        )
        def chat_message(self,event):
            text= event["text"]
            self.send(text_data=json.dumps({"text":text}))