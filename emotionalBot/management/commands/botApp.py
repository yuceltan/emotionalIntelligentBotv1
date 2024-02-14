from django.core.management.base import BaseCommand
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import csv
import os

class Command(BaseCommand):
    help = "Train ChatterBot with the Ubuntu Dialogue Corpus dataset"

    def handle(self, *args, **options):

        chatbot = ChatBot('UbuntuBot')

        dataset_dir = r'C:\Users\yucel\Downloads\archive (6)\Ubuntu-dialogue-corpus'

        if not os.path.isdir(dataset_dir):
            self.stdout.write(self.style.WARNING(f"Directory '{dataset_dir}' does not exist"))
            return


        for filename in os.listdir(dataset_dir):
            if filename.endswith('.csv'):
                file_path = os.path.join(dataset_dir, filename)
                with open(file_path, 'r', encoding='utf-8') as file:
                    reader = csv.DictReader(file)
                    dialogue = []
                    for row in reader:
                        text = row['text'].strip('"')
                        dialogue.append(text)
                    trainer = ListTrainer(chatbot)
                    trainer.train(dialogue)

        self.stdout.write(self.style.SUCCESS("ChatterBot trained with Ubuntu Dialogue Corpus dataset"))
