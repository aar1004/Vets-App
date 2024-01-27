import pymongo

uri = "mongodb+srv://aarchie:aarchie@cluster0.vzuenno.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(uri)
db = client["datascience"]
collections = db.list_collection_names()
for collection in collections:
    print(collection)

documents = db["collection1"].find()
for document in documents:
    print(document)
