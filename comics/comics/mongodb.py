import pymongo

# mongodb 모듈 생성
client = pymongo.MongoClient('mongodb://15.165.28.220:27017/') # mongodb ip 필요
db = client.comics
collection = db.dcinsidecomics
