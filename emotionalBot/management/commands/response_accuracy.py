import random
from chatterbot import ChatBot
import matplotlib.pyplot as plt

def evaluate_accuracy(chatterbot, test_data):
    correct_responses = 0
    total_responses = len(test_data)

    for query, expected_response in test_data:
        response = chatterbot.get_response(query)
        if response.text == expected_response:
            correct_responses += 1

    accuracy = (correct_responses / total_responses) * 100
    return accuracy

def plot_accuracy_over_time(accuracies):
    plt.plot(range(1, len(accuracies) + 1), accuracies)
    plt.xlabel('Training Iteration')
    plt.ylabel('Accuracy (%)')
    plt.title('ChatterBot Accuracy Over Time')
    plt.grid(True)
    plt.savefig('accuracy_graph.png')  # Save the graph to a file
    plt.show()

def train_and_evaluate():
    chatterbot = ChatBot('MyChatBot')

    # Test data consisting of input queries and expected responses
    test_data = [
        ("how are you?", "I am on the internet "),
        ("i am sad", "i sometimes feel disheartened when i realise just how far from my own culture i am sadness"),
        ("What is your name", "My name is E.S.I.B.A"),
        ("I am in love",
         "i out of all people really dont have many proplems talking about how i feel that being said i am in love so after all i have bitched about the last months was in vain sadness"),
        ("I feel romantic", "i feel romantic too love"),
        ("what school do you go to?", 'i ve been good. i m in school right now. what school do you go to?'),
    ]

    num_iterations = 10
    accuracies = []
    for i in range(num_iterations):
        random.shuffle(test_data)
        accuracy = evaluate_accuracy(chatterbot, test_data)
        accuracies.append(accuracy)
        print(f"Iteration {i + 1} Accuracy: {accuracy:.2f}%")

    # Plot accuracy over time
    plot_accuracy_over_time(accuracies)

if __name__ == "__main__":
    train_and_evaluate()
