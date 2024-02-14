from django.core.management.base import BaseCommand
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import pandas as pd
from chatterbot.ext.django_chatterbot import settings


class Command(BaseCommand):
    help = "Train ChatterBot with corpus data"

    def handle(self, *args, **options):
        df = pd.read_csv(
            r'C:\Users\yucel\Documents\MY PROJECTS\emotionalIntelligentBotv1\emotionalBot\Emotion_final.csv')

        conversations = []
        for index, row in df.iterrows():
            text = row['Text']
            emotion = row['Emotion']
            conversation = text + " " + emotion
            conversations.append(conversation)

        chatterbot = ChatBot(**settings.CHATTERBOT_SETTINGS)

        trainer = ListTrainer(chatterbot)
        trainer.train(conversations)

        self.stdout.write(self.style.SUCCESS("ChatterBot trained with corpus data"))
