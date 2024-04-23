
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

url ="mongodb+srv://Rasma:Taipan_2442@clustermatt.3tir65q.mongodb.net/?retryWrites=true&w=majority&appName=ClusterMatt"


def con():
    cliente = MongoClient(url, server_api = ServerApi('1'))
    try:
        cliente.admin.command('ping')
        print("Conectados a Mongo Usando python.. XD :D")
        db = cliente.sede
        return(db)
    except Exception as e:
        print(e)