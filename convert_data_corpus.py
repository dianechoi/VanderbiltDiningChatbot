import json

from pymongo import MongoClient
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from kubernetes import client, config
import yaml
import time


config.load_incluster_config()
api = client.CoreV1Api()
time.sleep(0.1)
service = api.read_namespaced_service(name="mongo-nodeport-svc", namespace='default')
ipMongodb = service.spec.cluster_ip

CONNECTION_STRING = 'mongodb://elliot:erindiane@' + ipMongodb + ":27017"

# Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
client = MongoClient(CONNECTION_STRING)
dbnames = client.list_database_names()
if 'training' in dbnames:
    client.drop_database("training")
db = client["training"]

chatbot = ChatBot(
    'My Chatterbot',
    storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
    #database_uri='mongodb://elliot:erindiane@' + ipMongodb + ":27017/training?authSource=admin",
    database_uri='mongodb://elliot:erindiane@' + ipMongodb + ":27017/training?authSource=admin", # refresh data each time chatbot is run 
    logic_adapters=[{
        'import_path': 'chatterbot.logic.BestMatch',
        'default_response': 'I am sorry, but I do not understand.',
    }
    ],
    read_only=True # prevents chatbot from learning from user's input
)



corpus = dict()


temp = ["food", "dining halls"]
tempDict = {"categories":temp}
corpus["categories"] = temp

temp = []

reference = {
    "2301 breakfast": breakfast_2301_dict,
    "2301 daily offerings": daily_offerings_2301_dict
}


dining_halls_corpus = ["2301 breakfast", "2301 daily offerings", "rand breakfast", "rand lunch", "commons breakfast", "commons lunch", "commons dinner", "commons daily offerings", "kissam breakfast", "kissam lunch", "kissam dinner", "kissam daily offerings", "ebi breakfast", "ebi lunch", "ebi dinner", "ebi daily offerings", "roth breakfast", "roth lunch", "roth dinner", "roth daily offerings", "zeppos breakfast", "zeppos lunch", "zeppos dinner", "zeppos daily offerings"]
for option in dining_halls_corpus:
    q = "What are the serving for " + option + "?"
    a = "They are serving the following: "
    foods = 's, '.join(list(reference[option].keys()))
    a += foods
    qa = [q, a]
    temp.append(qa)

tempDict = {"conversations":temp}
#corpus.append(tempDict)
corpus["conversations"] = temp

with open(r'/app/training_data.yaml', 'w+') as file:
    documents = yaml.dump(corpus, file)



trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train(
    "/app/VanderbiltDiningChatbot/training_data.yaml"
)

