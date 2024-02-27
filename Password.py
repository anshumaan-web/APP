! pip install pymongo

from pymongo import MongoClient

client = MongoClient()
dbname = client["First-Database"]
collection_name = dbname["Item Details"]

class student:
    def __init__(self, name, username, **kwargs):
        self.name = name
        self.username = username
        self.kwargs = kwargs

s1 = student("Anshumaan Mohanty","anshumaanrinku",college="GIETU", dept="CSE",campus="Gunupur")

collection_name.insert_one(vars(s1))
