from pymongo import MongoClient, errors
import os

MONGOUSER = os.getenv('MONGOUSER')
MONGOPASS = os.getenv('MONGOPASS')
MONGOHOST = os.getenv('MONGOHOST')
client = MongoClient(MONGOHOST, username=MONGOUSER, password=MONGOPASS, connectTimeoutMS=200, retryWrites=True)

db = client["ucu8tt"]

collection = db["Classes"]

classes = [{"code": "DS2002", "title": "Data Systems", "credits": 3},
           {"code": "CS3130", "title": "Computer System & Organization", "credits": 4}
           ,{"code": "CS3120", "title": "Discrete Mathematics", "credits": 3}
           ,{"code": "APMA3080", "title": "Linear Algebra", "credits": 3}
           , {"code": "ECE2200", "title": "Applied Physics 2", "credits": 4}]
collection.insert_many(classes)

results = collection.find({"credits": 3}).limit(3)

for item in results:
    print(item["title"])


