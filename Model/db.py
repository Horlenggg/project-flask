from pymongo import MongoClient
from applications import MONGO_URL,DATABASE_NAME


client = MongoClient(MONGO_URL)


db  = client[DATABASE_NAME]