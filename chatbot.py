import nltk
from nltk.chat.util import Chat, reflections

# Download required NLTK data (run once)
nltk.download('punkt')

# Define chatbot patterns and responses
pairs = [
    [
        "(hi|hello|hey)",
        ["Hello! How can I help you today?", "Hi there!"]
    ],
    [
        "what is your name\??",
        ["I am an AI chatbot created using Python and NLP."]
    ],
    [
        "how are you\??",
        ["I'm doing great! How can I assist you?"]
    ],
    [
        "what can you do\??",
        ["I can answer simple questions using Natural Language Processing."]
    ],
    [
        "(who is your creator|your creator)\??",
        ["I was created by a Python developer using NLP techniques."]
    ],
    [
        "(bye|exit|quit)",
        ["Goodbye! Have a nice day "]
    ],
    [
        "(.*)",
        ["Sorry, I didn't understand that. Can you rephrase?"]
    ]
]

# Create chatbot
chatbot = Chat(pairs, reflections)

# Start chatbot
print(" AI Chatbot using NLP")
print("Type 'bye' to exit\n")
chatbot.converse()
