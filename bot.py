from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot import comparisons
from chatterbot import response_selection
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from kubernetes import client, config
from flask_apscheduler import APScheduler
from apscheduler.schedulers.background import BackgroundScheduler
from chatterbot.comparisons import LevenshteinDistance

from pymongo import MongoClient
import time
import random
import string
import sys

class Config:
    SCHEDULER_API_ENABLED = True


app = Flask(__name__)
app.config.from_object(Config())

scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()

i = 0
timer = 60

config.load_incluster_config()
api = client.CoreV1Api()
time.sleep(0.1)
service = api.read_namespaced_service(name="mongo-nodeport-svc", namespace='default')
ipMongodb = service.spec.cluster_ip

print("it's working", file=sys.stdout)

class Comparator:

    def __init__(self, language):

        self.language = language

    def __call__(self, statement_a, statement_b):
        return self.compare(statement_a, statement_b)

    def compare(self, statement_a, statement_b):
        statement_a = str(statement_a).lower()
        statement_b = str(statement_b).lower()
        print(statement_a, file=sys.stdout)
        print(statement_b, file=sys.stdout)
        dining_halls_corpus = ["2301 breakfast", "2301 Daily Offerings", "rand breakfast", "rand lunch", "commons breakfast", "commons lunch", "commons dinner", "commons Daily Offerings", "kissam breakfast", "kissam lunch", "kissam dinner", "kissam Daily Offerings", "ebi breakfast", "ebi lunch", "ebi dinner", "ebi Daily Offerings", "roth breakfast", "roth lunch", "roth dinner", "roth Daily Offerings", "zeppos breakfast", "Zeppos Lunch", "Zeppos Dinner", "Zeppos Daily Offerings", "The Pub", "Rand Grab & Go Market", "Branscomb Munchie", "Commons Munchie", "Highland Munchie", "Kissam Munchie", "Local Java"]
        for phrase in dining_halls_corpus:
            words = phrase.split(' ')
            exact = True
            for i in words:
                word = i.lower()
                if word in statement_a:
                    if word not in statement_b:
                        exact = False
                else:
                    exact = False
            if exact:
                return 1.0
        return 0.0            
        similarity = LevenshteinDistance().compare(statement_a.text, statement_b.text)
        
        return similarity

chatbot = ChatBot(
    'My Chatterbot',
    storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
    database_uri='mongodb://elliot:erindiane@' + ipMongodb + ":27017/training?authSource=admin",
    # refresh data each time chatbot is run
    # logic_adapters=[{
    #     'import_path': 'chatterbot.logic.BestMatch',
    #     'default_response': 'I am sorry, but I do not understand.',
    #     'statement_comparison_function': keyword_weighted_comparison,
    #     'response_selection_method': response_selection.get_random_response,
    #     'maximum_similarity_threshold': 1.0
    # }
    # ],
    statement_comparison_function=Comparator.compare,
    read_only=True  # prevents chatbot from learning from user's input
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
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train(
    "/app/greetings_corpus.yml",
)


# # Terminal
# exit_conditions = (":q", "quit", "exit")
# while True:
#     query = input("> ")
#     if query in exit_conditions:
#         break
#     else:
#         print(f"{chatbot.get_response(query)}")

#@scheduler.task('interval', id='do_job_1', seconds=1, misfire_grace_time=900)
def job1():
    global timer
    timer -= 1
    if timer <= 0:
        f = open('/etc/hostname')
        pod_name = f.read()
        f.close()
        pod_name_list = pod_name.split('-')
        pod_id = pod_name_list[2]
        service_name = "bot-service-" + pod_id
        deployment_name = pod_name_list[0] + "-" + pod_name_list[1] + "-" + pod_name_list[2]
        config.load_incluster_config()
        api_service = client.CoreV1Api()
        api_deployment = client.AppsV1Api()
        time.sleep(0.1)
        service_result = api_service.delete_namespaced_service(name=service_name, namespace='default')
        deployment_result = api_deployment.delete_namespaced_deployment(name=deployment_name, namespace='default')

        # pod_result = api_pod.delete_namespaced_pod(name = pod_name, namespace='default')


s = string.ascii_uppercase + '0123456789'
chat_id = ''.join(random.choice(s) for i in range(20))


# Browser
# define app routes
@app.route("/")
def index():
    global chat_id
    return render_template("chatbot.html", id=chat_id)


CONNECTION = 'mongodb://elliot:erindiane@' + ipMongodb + ":27017"
mongoClient = MongoClient(CONNECTION)
db = mongoClient["history"]
col = db[chat_id]


@app.route("/get")
# function for the bot response
def get_bot_response():
    global timer
    global chat_id
    global db
    global col
    timer = 60
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
    scheduler = BackgroundScheduler()
    scheduler.add_job(func=job1, trigger="interval", seconds=2)
    scheduler.start()

    # app.run()
    app.run(debug=True, host='0.0.0.0')
