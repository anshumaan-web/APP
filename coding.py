from pymongo import MongoClient

client = MongoClient()
dbname = client["First-Database"]
collection_name = dbname["Student Details"]

class personal:
    def __init__(self):
        self.city = "Gunupur"
        self.state = "Odisha"
        self.pin = "765022"
        self.country = "India"

class student(personal):
    def __init__(self, name, dept):
        self.name = name
        self.dept = dept
        self.college_details = vars(personal())

s1 = student("Anshumaan Mohanty","CSE")
collection_name.insert_one(vars(s1)) 