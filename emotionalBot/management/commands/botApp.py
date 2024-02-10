from django.core.management.base import BaseCommand
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer
from chatterbot.ext.django_chatterbot import settings
from convokit import Corpus, download
from datasets import load_dataset

from emotionalBot.models import Statement



class Command(BaseCommand):
    help = "Train ChatterBot with corpus data and user feedback from MongoDB via Django model"

    def handle(self, *args, **options):
        bot = ChatBot('Emotional Intelligent Bot')

        training_data = Statement.objects.all()

        trainer = ListTrainer(bot)
        for statement in training_data:
            user_input = statement.in_response_to
            bot_response = statement.text
            feedback = statement.feedback
            trainer.train([f"{user_input}\t{bot_response}\t{feedback}"])

        print("Bot training completed.")

        print("Bot is ready. You can start interacting.")
        while True:
            user_input = input("You: ")
            bot_response = bot.get_response(user_input)
            print("Bot:", bot_response)
            feedback = input("Was this response helpful? (yes/no): ")

            statement = Statement.objects.create(
                in_response_to=user_input,
                text=bot_response,
                feedback=feedback
            )
            statement.save()

            if feedback.lower() == 'no':
                updated_training_data = Statement.objects.all()
                updated_chats = [
                    f"{data.in_response_to}\t{data.text}\t{data.feedback}"
                    for data in updated_training_data
                ]
                trainer.train(updated_chats)