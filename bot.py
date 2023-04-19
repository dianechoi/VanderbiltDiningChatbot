from flask import Flask, render_template, request
import random
import string
from pymongo import MongoClient
# from chatterbot import ChatBot
# from chatterbot.trainers import ListTrainer
# from chatterbot.trainers import ChatterBotCorpusTrainer

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

s = string.ascii_uppercase + '0123456789'
chat_id = ''.join(random.choice(s) for i in range(20))


# Browser
# define app routes
@app.route("/")
def index():
    global chat_id
    return render_template("chatbot.html", id=chat_id)


CONNECTION = "mongodb://elliot:erindiane@129.114.26.125:8080"
client = MongoClient(CONNECTION)
db = client["history"]
col = db[chat_id]


@app.route("/get")
# function for the bot response
def get_bot_response():
    global chat_id
    global CONNECTION
    global client
    global db
    global col
    chat_data = dict()
    user_text = "" + request.args.get('msg')
    response = str(chatbot.get_response(user_text))
    chat_data["user"] = user_text
    chat_data["bot"] = response
    print(chat_data)
    col.insert_one(chat_data)
    return response


@app.route("/lookup.html")
def lookup():
    return render_template("lookup.html")


@app.route("/id")
def get_chat_convo():
    global CONNECTION
    global client
    global db
    global col
    user_input_id = request.args.get('msg')
    col = db[user_input_id]
    cursor = col.find({}, {'_id': False})
    chat_data = []
    count = 0
    for x in cursor:
        obj = f"'{count}': {str(x)}"
        chat_data.append(obj)
        count += 1
    chat_data = '{' + str(chat_data)[1:-1] + '}'
    return chat_data


if __name__ == "__main__":
    # app.run()
    app.run(debug=True, host='0.0.0.0')