import matplotlib.pyplot as plt
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import pandas as pd
from django.core.management.base import BaseCommand

def calculate_accuracy(chatbot, test_data):
    correct = 0
    accuracy_values = []

    for query, expected_response in test_data:
        bot_response = chatbot.get_response(query).text
        if bot_response == expected_response:
            correct += 1
        accuracy = correct / len(test_data) * 100
        accuracy_values.append(accuracy)

    return accuracy_values

class Command(BaseCommand):
    help = "Train ChatterBot with corpus data"

    def handle(self, *args, **options):
        df = pd.read_csv(
            r'C:\Users\yucel\Documents\MY PROJECTS\emotionalIntelligentBotv1\emotionalBot\Datasets\Conversation.csv')

        conversations = []
        for index, row in df.iterrows():
            question = row['question']
            answer = row['answer']
            conversation = f"{question} {answer}"  # Concatenate question and answer
            conversations.append(conversation)

        chatterbot = ChatBot("E.S.I.B.A")

        trainer = ListTrainer(chatterbot)
        trainer.train(conversations)

        test_data = [
            ("how are you?", "I am on the internet "),
            ("i am sad", "i sometimes feel disheartened when i realise just how far from my own culture i am sadness"),
            ("What is your name", "My name is E.S.I.B.A"),
            ("I am in love","i out of all people really dont have many proplems talking about how i feel that being said i am in love so after all i have bitched about the last months was in vain sadness"),
            ("I feel romantic", "i feel romantic too love"),
            ("what school do you go to?", 'i ve been good. i m in school right now. what school do you go to?'),
        ]

        accuracy_values = calculate_accuracy(chatterbot, test_data)

        plt.plot(accuracy_values)
        plt.title('ChatterBot Response Accuracy Over Time')
        plt.xlabel('Number of Queries')
        plt.ylabel('Accuracy (%)')
        plt.grid(True)
        plt.show()

        self.stdout.write(self.style.SUCCESS("ChatterBot trained with corpus data"))
