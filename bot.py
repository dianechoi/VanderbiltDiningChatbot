from flask import Flask, render_template, url_for, request, redirect
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

class Config:
    SCHEDULER_API_ENABLED = True


app = Flask(__name__)
app.config.from_object(Config())

scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()

i = 0
timer = 300

config.load_incluster_config()
api = client.CoreV1Api()
time.sleep(0.1)
service = api.read_namespaced_service(name="mongo-nodeport-svc", namespace='default')
ipMongodb = service.spec.cluster_ip

dining_halls_corpus = [
    # Dining halls - Options
    "2301 breakfast options",
    "2301 daily offerings options",
    "Rand breakfast options",
    "Rand lunch options",
    "Commons breakfast options",
    "Commons lunch options",
    "Commons dinner options",
    "Commons daily offerings options",
    "Kissam breakfast options",
    "Kissam lunch options",
    "Kissam dinner options",
    "Kissam daily offerings options",
    "EBI breakfast options",
    "EBI lunch options",
    "EBI dinner options",
    "EBI daily offerings options",
    "Rothschild breakfast options",
    "Rothschild lunch options",
    "Rothschild dinner options",
    "Rothschild daily offerings options",
    "The Pub daily offerings options",
    "Zeppos breakfast options",
    "Zeppos lunch options",
    "Zeppos dinner options",
    "Zeppos daily offerings options",
    # Dining halls - Ingredients
    "2301 breakfast ingredients",
    "2301 daily offerings ingredients",
    "Rand breakfast ingredients",
    "Rand lunch ingredients",
    "Commons breakfast ingredients",
    "Commons lunch ingredients",
    "Commons dinner ingredients",
    "Commons daily offerings ingredients",
    "Kissam breakfast ingredients",
    "Kissam lunch ingredients",
    "Kissam dinner ingredients",
    "Kissam daily offerings ingredients",
    "EBI breakfast ingredients",
    "EBI lunch ingredients",
    "EBI dinner ingredients",
    "EBI daily offerings ingredients",
    "Rothschild breakfast ingredients",
    "Rothschild lunch ingredients",
    "Rothschild dinner ingredients",
    "Rothschild daily offerings ingredients",
    "The Pub daily offerings ingredients",
    "Zeppos breakfast ingredients",
    "Zeppos lunch ingredients",
    "Zeppos dinner ingredients",
    "Zeppos daily offerings ingredients"
] 
munchies_corpus = [
    "Rand Grab & Go Market",
    "Branscomb Munchie",
    "Commons Munchie",
    "Highland Munchie",
    "Kissam Munchie",
    "Local Java"
]
dining_halls_hours_corpus = [        
    "2301 hours",
    "Rand hours",
    "Commons hours",
    "Kissam hours",
    "EBI hours",
    "Rothschild hours",
    "Pub hours",
    "Zeppos hours"
]
def response_selector(input_statement, response_list, storage=None):
    global dining_halls_corpus
    global munchies_corpus
    global dining_halls_hours_corpus
    total_list = dining_halls_corpus + munchies_corpus + dining_halls_hours_corpus
    statement_d = input_statement
    for statement_c in response_list:
        statement_a = str(statement_d.text).lower()
        statement_b = str(statement_c.text).lower()
        for phrase in total_list:
            words = phrase.split(' ')
            exact = True
            for i in words:
                word = i.lower()
                if word in statement_a.lower():
                    if word not in statement_b.lower():
                        exact = False
                else:
                    exact = False
            if exact:
                return statement_c
    statement_d.text = "Sorry, I could not understand. Please format your question in the following way: 'What is [Dining Hall] [Breakfast/Lunch/Dinner/Daily Offerings] serving today?'"
    return statement_d        

chatbot = ChatBot(
    'My Chatterbot',
    storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
    database_uri='mongodb://elliot:erindiane@' + ipMongodb + ":27017/training?authSource=admin",
    response_selection_method=response_selector,
    read_only=True  # prevents chatbot from learning from user's input
)

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


s = string.ascii_uppercase + '0123456789'
chat_id = 'A' + ''.join(random.choice(s) for i in range(20))


# Browser
@app.route("/")
def index():
    global chat_id
    return render_template("chatbot.html", id=chat_id)


CONNECTION = 'mongodb://elliot:erindiane@' + ipMongodb + ":27017"
mongoClient = MongoClient(CONNECTION)
db = mongoClient["history"]
col = db[chat_id]


@app.route("/get")
def get_bot_response():
    global timer
    global chat_id
    global db
    global col
    timer = 300
    chat_data = dict()
    user_text = "" + request.args.get('msg')
    response = str(chatbot.get_response(user_text))
    response = response.replace("\'", '')
    chat_data["user"] = user_text
    chat_data["bot"] = response
    print(chat_data)
    col.insert_one(chat_data)
    return response


@app.route("/index.html")
def home():
    return redirect(f'http://129.114.26.125:30001', code=302)


@app.route("/lookup.html")
def lookup():
    return render_template("lookup.html")


@app.route("/id")
def get_chat_convo():
    global CONNECTION
    global db
    user_input_id = request.args.get('msg')
    getCol = db[user_input_id]
    cursor = getCol.find({}, {'_id': False})
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
