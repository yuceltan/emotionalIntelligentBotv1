import matplotlib.pyplot as plt
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.response_selection import get_most_frequent_response
from django.core.management.base import BaseCommand

def calculate_accuracy(chatbot, test_data):
    correct = 0
    accuracy_values = []

    for query, expected_response in test_data:
        bot_response = chatbot.get_response(query)
        if bot_response.text == expected_response:
            correct += 1
        accuracy = correct / len(test_data) * 100
        accuracy_values.append(accuracy)

    return accuracy_values

class Command(BaseCommand):
    help = "Train ChatterBot with corpus data"

    def handle(self, *args, **options):
        chatterbot = ChatBot("E.S.I.B.A", response_selection_method=get_most_frequent_response)
        trainer = ChatterBotCorpusTrainer(chatterbot)
        trainer.train("chatterbot.corpus.english")

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
