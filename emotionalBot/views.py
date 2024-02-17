from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpRequest, JsonResponse, HttpResponse
from django.views.generic import View, TemplateView
from django.core.serializers import serialize
from django import forms
from django.contrib.auth import authenticate, login, logout

from chatterbot import ChatBot
from requests import request
import response
from django.contrib.auth.models import User

class Registration(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class ViewApp(TemplateView):
    template_name = 'index.html'

def home(request):
    return render(request, 'chat.html')

def bot_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def bot_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            nameUser = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=nameUser, password=password)
            if user:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def bot_logout(request):
    logout(request)
    return redirect('login')

# Add your other views or classes here...


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
