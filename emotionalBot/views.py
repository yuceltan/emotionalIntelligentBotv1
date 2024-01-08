from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse

def view_app(request):
    return HttpResponse(r'C:\Users\yucel\Documents\MY PROJECTS\emotionalIntelligentBotv1\templates\frontEnd\index.html')



