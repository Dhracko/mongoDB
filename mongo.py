import pymongo
import os
from os import path
if path.exists("env.py"):
  import env 

# Define the varibles for connection

MONGODB_URI = os.environ.get('MONGO_URI')
DBS_NAME = "myTestDB"
COLLECTION_NAME = "myFirstMDB"

# Def a function to connect to MongoDB
def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected!")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print ("Could not connect to MongoDB: %s") % e

conn = mongo_connect(MONGODB_URI)

coll = conn[DBS_NAME][COLLECTION_NAME]

# new_doc = {'first': 'douglas', 'last': 'adams', 'dob': '11/03/1952', 'hair_colour': 'grey', 'occupation': 'writer', 'nationality': 'english'}

# coll.insert_one(new_doc)


# coll.remove({'first': 'douglas'})
# coll.update_one({'nationality': 'american'}, {'$set': {'hair_colour': 'maroon'}})

coll.update_many({'nationality': 'american'}, {'$set': {'hair_colour': 'maroon'}})


documents = coll.find({'nationality': 'american'})

for doc in documents:
    print(doc)
