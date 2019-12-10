import pymongo

client = pymongo.MongoClient('mongodb://15.165.28.220:27017/')
db = client.comics
collection = db.bestcomiecs
