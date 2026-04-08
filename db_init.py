from pymongo import MongoClient

def database_connect():
    log = MongoClient("mongodb://localhost:27017/")
    db = log["database"]
    return db
    
def database(choice):
    database = database_connect()
    collection = database[choice]
    return collection




