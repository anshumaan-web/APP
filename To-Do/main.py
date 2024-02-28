import streamlit as st
from streamlit_extras.grid import grid
from pymongo import MongoClient

client = MongoClient()
db_name = client["To-Do"]
collection_name = db_name["list-of-to-do-s"]

dummy_data = [
    {"task": "simple Task 1", "isdone": True},
    {"task": "simple Task 2", "isdone": False},
    {"task": "simple Task 3", "isdone": True},
    {"task": "simple Task 4", "isdone": False}
]

class tasks(data, state):
    def __init__(self, tasks, isdonr=False):
        self.task = task
        self.isdone = isdone

def tasks(data, state):
    st.checkbox(data, value=state)

def layout():
    my_grid = grid([5,1], vertical_align="bottom")
    data = my_grid.text_input("Enter the Data", label_visibility="hidden")
    if my_grid.button("Added"):
        if data != "":
            tasks_oj = task(data)
            collection_name.insert_one(vars(tasks_oj))
            st.success("Data Added Successfully.")
        else:
            st.warning("please Enter the task.")  

st.title("To-Do List App")
layout()

for i in dummy_data:
    tasks(data=i["task"], state=i["isdone"])