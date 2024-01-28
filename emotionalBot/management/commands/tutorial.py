# to teach the model,users will upload the conversation sets over here.
from django.core.management.base import BaseCommand
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.ext.django_chatterbot import settings
import spacy
from emotionalBot.models import TrainData
#from spacy.cli.download import download
#download(model="en_core_web_sm")



class Command(BaseCommand):
    data = "TEST"

    def handle(self, *args, **options):


        chatterbot = ChatBot(**settings.CHATTERBOT_SETTINGS)
        tutor = ListTrainer(chatterbot)
        tutor.train(
           [
               "Hello",
               "Hi there!",
               "How are you doing?",
               "I'm doing great.",
               "That is good to hear",
               "Thank you.",
               "You're welcome.",
           ]
                    )
        self.stdout.write(self.style.SUCCESS("Training Successfully Completed "))
