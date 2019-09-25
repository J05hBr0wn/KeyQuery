import pymongo

client = pymongo.MongoClient("<reference to MongoDB Atlas database>")
db = client.get_database("<database_name>")
collection = db.get_collection('<collection_name>')
collection.remove()

