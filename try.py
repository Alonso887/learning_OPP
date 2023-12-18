import pymongo
import datetime
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://LaEntropia:GwsItEDiNC7Jmaq3@twikker.xkiwhwx.mongodb.net/?retryWrites=true&w=majority")
db = cluster["Twikker"]
collection = db["Posts"]


def divide_posts(documents_list):
    return [documents_list[i:i+12] for i in range(0,len(documents_list),12)]

all_documents = []
for document in collection.find():
    all_documents.append(document)
all_documents.reverse()
pages = divide_posts(all_documents)
print(len(pages[1]))


