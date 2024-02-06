from django.core.management.base import BaseCommand
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer
from chatterbot.ext.django_chatterbot import settings

class Command(BaseCommand):
    help = "Train ChatterBot with corpus data"
    def handle(self, *args, **options):
        chatterbot = ChatBot(**settings.CHATTERBOT_SETTINGS)
        trainer = ListTrainer(chatterbot)
        trainer.train([
                "Hello",
                "Hi there!",
                "How are you doing?",
                "I'm doing great.",
                "That is good to hear",
                "Thank you.",
                "You're welcome.",
            ]
)
        self.stdout.write(self.style.SUCCESS("ChatterBot trained with corpus data"))
