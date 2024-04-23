
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

url ="mongodb+srv://Darkilling:H3r0g4m3rs@clusterluis.hquplkv.mongodb.net/?retryWrites=true&w=majority&appName=clusterluis"


def con():
    cliente = MongoClient(url, server_api = ServerApi('1'))
    try:
        cliente.admin.command('ping')
        print("Conectados a Mongo Usando python.. XD :D")
        db = cliente.sample_restaurants
        return(db)
    except Exception as e:
        print(e)