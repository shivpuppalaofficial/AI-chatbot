# ai_chatbot.py
from nltk.chat.util import Chat, reflections

pairs = [
    ["hi|hello|hey", ["Hello!", "Hi there!", "Hey!"]],
    ["how are you ?", ["I'm doing well, thank you!", "All good! How about you?"]],
    ["what is your name ?", ["I'm a chatbot created by you!"]],
    ["bye|goodbye", ["Goodbye!", "See you soon!"]],
]

chatbot = Chat(pairs, reflections)
print("🤖 AI Chatbot: Type 'quit' to exit")
chatbot.converse()
