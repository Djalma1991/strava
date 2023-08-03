from api import Athlete, Activity
from db import Athletes, Tokens, Activities
import json


def save_athlete():
    db = Athletes()
    api = Athlete(athlete_id=65927882)
    data = api.get()
    save_data = db.insert(data)
    return save_data


def write_db(data: dict):
    db = Tokens()
    id = data.pop("athlete").get("id")
    if db.select(id=id):
        db.update(values=data, id=id)
    else:
        data.update({"id": id})
        db.insert(values=data)

def activities():   
    api = Activity(athlete_id=65927882)
    data = api.get(activity_id=9536701630)
    return data

def write_activity(data: dict):
    db = Activities()
    data_ = json.loads(data.json())
    id = data_.pop("id")
    if db.select(id=id):
        db.update(data=data)
    else:
        data.update({"id": id})
        db.insert(data_=data)