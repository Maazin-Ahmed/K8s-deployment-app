#mongo connection

from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["eivor"]
collection = db["names"] 