import pymongo

mongoURI = "mongodb://localhost:27017/"

client = pymongo.MongoClient(mongoURI)

db = client["TODO"]
collection = db["todo"]