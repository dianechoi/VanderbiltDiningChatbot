from flask import Flask, render_template, request
# import spacy
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer


# spacy.load("en")
app = Flask(__name__)

chatbot = ChatBot(
    'My Chatterbot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///db.sqlite3', # refresh data each time chatbot is run 
    logic_adapters=[{
        'import_path': 'chatterbot.logic.BestMatch',
        'default_response': 'I am sorry, but I do not understand.',
    }
    ], 
    read_only=True # prevents chatbot from learning from user's input
)


# # ListTrainer
# trainer = ListTrainer(chatbot)
# trainer.train([
#     "What are the hours for Rand dining hall?",
#     "The hours for Rand dining hall are 7:00 AM to 3:00 PM Monday-Friday and closed Saturday-Sunday.",
#     "What food is Rand dining hall serving for lunch today?",
#     "The various options Rand dining hall serves are: Chef James Bistro, Salad Bar, Bakery, Randwich, Fresh Mex, Soup, Mongolian Grill, Mediterranean, Beverages, Fruit, Alternative Cooler, Condiments, and Self-Serve. Which would you like to see in more detail?"
# ])

# CorpusTrainer
# trainer = ChatterBotCorpusTrainer(chatbot)
# trainer.train(
#     "/app/greetings_corpus.yml",
#     "/app/dining_corpus.yml"
# )

# # Terminal
# exit_conditions = (":q", "quit", "exit")
# while True:
#     query = input("> ")
#     if query in exit_conditions:
#         break
#     else:
#         print(f"{chatbot.get_response(query)}")

# Browser
#define app routes
@app.route("/")
def index():
    return render_template("chatbot.html")

@app.route("/get")
#function for the bot response
def get_bot_response():
    userText = request.args.get('msg')
    return str(chatbot.get_response(userText))

if __name__ == "__main__":
    # app.run()
    app.run(debug=True, host='0.0.0.0')