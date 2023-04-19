from pymongo import MongoClient
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from kubernetes import client, config
import yaml
import time


# config.load_incluster_config()
# api = client.CoreV1Api()
# time.sleep(0.1)
# service = api.read_namespaced_service(name="mongo-nodeport-svc", namespace='default')
# ipMongodb = service.spec.cluster_ip

CONNECTION_STRING = "mongodb://elliot:erindiane@129.114.26.125:8080"

# Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
client = MongoClient(CONNECTION_STRING)
client.drop_database("training")
db = client["training"]

chatbot = ChatBot(
    'My Chatterbot',
    storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
    #database_uri='mongodb://elliot:erindiane@' + ipMongodb + ":27017/training?authSource=admin",
    database_uri='mongodb://elliot:erindiane@129.114.26.125:8080/training?authSource=admin',
    logic_adapters=[{
        'import_path': 'chatterbot.logic.BestMatch',
        'default_response': 'I am sorry, but I do not understand.',
    }
    ],
    read_only=True # prevents chatbot from learning from user's input
)



corpus = []

dict_file = [{'sports' : ['soccer', 'football', 'basketball', 'cricket', 'hockey', 'table tennis']},
{'countries' : ['Pakistan', 'USA', 'India', 'China', 'Germany', 'France', 'Spain']}]

temp = ["food"]
tempDict = {"categories":temp}
corpus.append(tempDict)

temp = []

breakfast_2301_dict = {}
daily_offerings_2301_dict = {}
breakfast_2301_dict["smoothie"] = ["arugala", "blueberries"]
breakfast_2301_dict["bowl"] = ["chicken", "rice"]
daily_offerings_2301_dict["nut"] = ["boop", "shmoop"]
daily_offerings_2301_dict["cracker"] = ["top", "mop"]

temp_dining_halls = ["2301 breakfast", "2301 daily offerings"]
reference = {
    "2301 breakfast": breakfast_2301_dict,
    "2301 daily offerings": daily_offerings_2301_dict
}


dining_halls = ["2301 breakfast", "2301 daily offerings", "rand breakfast", "rand lunch", "commons breakfast", "commons lunch", "commons dinner", "commons daily offerings", "kissam breakfast", "kissam lunch", "kissam dinner", "kissam daily offerings", "ebi breakfast", "ebi lunch", "ebi dinner", "ebi daily offerings", "roth breakfast", "roth lunch", "roth dinner", "roth daily offerings", "zeppos breakfast", "zeppos lunch", "zeppos dinner", "zeppos daily offerings"]
for option in temp_dining_halls:
    q = "What are the serving for " + option + "?"
    a = "They are serving the following: "
    foods = 's, '.join(list(reference[option].keys()))
    a += foods
    qa = [q, a]
    temp.append(qa)

tempDict = {"conversations":temp}
corpus.append(tempDict)

with open(r'~/training_data.yaml', 'w') as file:
    documents = yaml.dump(corpus, file)





trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train(
    "training_data.yaml"
)
#
#
# # This is added so that many files can reuse the function get_database()
# if __name__ == "__main__":
#
#
   # CONNECTION_STRING = "mongodb://elliot:erindiane@129.114.26.125:8080"
   #
   # # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
   # client = MongoClient(CONNECTION_STRING)
   # db = client["history"]
#    col = db["OKWVN596MLY525D3IU7H"]
#    cursor = col.find({})
#    for x in cursor:
#       print(x)
#    print(db.list_collection_names())
#    print(client.list_database_names())

