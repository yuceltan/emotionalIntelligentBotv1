from django.core.management.base import BaseCommand
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.ext.django_chatterbot import settings

class Command(BaseCommand):
    help = "Train ChatterBot with corpus data"

    def handle(self, *args, **options):
        chatterbot = ChatBot(**settings.CHATTERBOT_SETTINGS)

        # Create a new trainer for the ChatterBot model
        trainer = ChatterBotCorpusTrainer(chatterbot)

        # Train the ChatterBot model with English language corpus data
        trainer.train("chatterbot.corpus.english")

        self.stdout.write(self.style.SUCCESS("ChatterBot trained with corpus data"))
