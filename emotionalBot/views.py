from django.shortcuts import render
from django.http import HttpRequest
from django.http import JsonResponse
from chatterbot import ChatBot
from django.http import HttpResponse
from django.views.generic import View
from chatterbot.ext.django_chatterbot import settings
from requests import request
import response

import json


def view_app(request):
    return render(request,
                  r'C:\Users\yucel\Documents\MY PROJECTS\emotionalIntelligentBotv1\templates\frontEnd\index.html')

    # HttpResponse does not render the index.html from views.py


class BotChat(View):
    emotionalBot = ChatBot(settings.CHATTERBOT_SETTINGS)

    def post(self, *args, **kwargs):  # to get any number of length from the input which is typed.
        input_data = json.loads(request.body.decode('utf-8'))
        if 'text' not in input:
            return JsonResponse({
                'text': ['Input must be entered to continue']

            }, status=400)
        response_data = self.chatterbot.get_response(input)
        chat_response = response.serialize()
        return JsonResponse(chat_response, status=200)

    def get(self, *args, **kwargs):
        # output =  json.loads(response,body.encode('utf-8')):
        return self.chatterbot.name
