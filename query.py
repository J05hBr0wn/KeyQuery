import pymongo
from collections import defaultdict

client = pymongo.MongoClient("<reference to MongoDB Atlas database>")
db = client.get_database("<database_name>")
collection = db.get_collection('<collection_name>')

print("\n ==================================== \n \t Language Diagnostics \n ==================================== \n")

print("Collection " + str(collection.full_name) + " has " + str(collection.count_documents({})) + " articles.\n")

query_count = { "message": { "$regex": "", "$options" :'i' } }

chars = defaultdict(int)

for msg in collection.find(query_count):
    for char in msg['message']:
        chars[char] += 1

for key in chars.keys():
    print("Letter '" + key + "' appeared in the query " + str(chars[key]) + " times")
print("")

messages = collection.find(query_count)
word_frequency = defaultdict(int)

for msg in messages:
    string = str(msg['message']).split(" ")
    for word in string:
        word_frequency[word] += 1

for key in word_frequency.keys():
    print("The word '" + str(key) + "' appeared " + str(word_frequency[key]) + " time(s)")

print("\n ==================================== \n \t     Manual Query \n ====================================  \n")

while True:   
    ipt = input("Enter the term to search for: (QUIT to exit) ")

    if ipt == "QUIT":
        break

    query = { "message": { "$regex": ipt, "$options" :'i' } }
    
    docs = collection.find(query)

    print ("query:", query)

    print ("$regex using $options 'i' -- total: \n ")

    for i in docs:
        print(i['date'] + " -> " + i['message'])
    print("")

    
    