from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.http import JsonResponse
from chatterbot import ChatBot
from django.http import HttpResponse
from django.views.generic import View, TemplateView
from chatterbot.ext.django_chatterbot import settings
from requests import request
import response
"""from models import TrainData"""

import json

from emotionalIntelligentBotv1.task import add

result = add.delay(4, 4)

class ViewApp(TemplateView):
    template_name = 'chat.html'



#class Home(View):
    #template_name = "C:\Users\yucel\Documents\MY PROJECTS\emotionalIntelligentBotv1\templates\frontEnd\emotionalbot.html"
    #def get(self,request):
        #return HttpResponse('C:\Users\yucel\Documents\MY PROJECTS\emotionalIntelligentBotv1\templates\frontEnd\emotionalbot.html')

    #def post(self,request):
        #return HttpResponse("Class based view")


"""def view_app(request):
    return render(request,
                  '')

    # HttpResponse does not render the index.html from views.py

def train_chat_Data(request):
    if request.method == 'POST':
        sender = request.POST.get('sender')
        message = request.POST.get('message')

        TrainData.objects.create(sender=sender,message=message)
    return redirect('home.html') #redirect to user after saved the messages successfully
    #another if else contidion will be added to if the system can not save the messages successfully
        #save the data in database

def get_back_messages(request):
    old_messages = TrainData.objects.all()
    return render(request, r'template/oldMessages.html',{'oldMessages':old_messages})"""
"""class BotChat(View):
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
        return self.chatterbot.name"""
