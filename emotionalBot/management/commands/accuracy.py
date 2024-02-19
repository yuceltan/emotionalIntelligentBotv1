from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

test_data = [
    ("how are you?", "I am on the internet "),
    ("i am sad", "i sometimes feel disheartened when i realise just how far from my own culture i am sadness"),
    ("What is your name", "My name is E.S.I.B.A"),
    ("I am in love",
     "i out of all people really dont have many proplems talking about how i feel that being said i am in love so after all i have bitched about the last months was in vain sadness"),
    ("I feel romantic", "i feel romantic too love"),
    ("what school do you go to?", 'i ve been good. i m in school right now. what school do you go to?'),
]

def preprocess_text(text):
    tokens = word_tokenize(text.lower())
    tokens = [word for word in tokens if word not in stopwords.words("english")]
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    return tokens

def evaluate_accuracy(chatterbot, test_data):
    correct_responses = 0
    total_responses = len(test_data)

    for query, expected_response in test_data:
        response = chatterbot.get_response(query)
        print(f"Query: {query}")
        print(f"Expected Response: {expected_response}")
        print(f"Actual Response: {response.text}")
        if similarity(preprocess_text(response.text), preprocess_text(expected_response)) > 0.8:
            correct_responses += 1

    accuracy = (correct_responses / total_responses) * 100
    return accuracy

def similarity(tokens1, tokens2):

    set1 = set(tokens1)
    set2 = set(tokens2)
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    if union == 0:
        return 0
    else:
        return intersection / union

def plot_accuracy_over_time(accuracies):
    plt.plot(range(1, len(accuracies) + 1), accuracies)
    plt.xlabel('Training Iteration')
    plt.ylabel('Accuracy (%)')
    plt.title('ChatterBot Accuracy Over Time')
    plt.savefig('accuracy_graph.png')
    plt.close()

def train_and_evaluate():
    chatterbot = ChatBot('MyChatBot')
    trainer = ChatterBotCorpusTrainer(chatterbot)
    trainer.train('chatterbot.corpus.english')

    num_iterations = 10
    accuracies = []
    for i in range(num_iterations):
        accuracy = evaluate_accuracy(chatterbot, test_data)
        accuracies.append(accuracy)
        print(f"Iteration {i+1} Accuracy: {accuracy:.2f}%")

    plot_accuracy_over_time(accuracies)

if __name__ == "__main__":
    train_and_evaluate()