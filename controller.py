from api import Athlete, Activity
from db import Athletes, Tokens, Activities
import json


def save_athlete(athlete_id):
    api = Athlete(athlete_id)
    data = api.get()
    return print(data)


def write_athlete(data: dict):
    db = Tokens()
    id = data.pop("athlete").get("id")
    if db.select(id=id):
        db.update(values=data, id=id)
    else:
        data.update({"id": id})
        db.insert(values=data)

def activities(activity_id: int, athlete_id: int) -> dict:   
    api = Activity(athlete_id=athlete_id, activity_id=activity_id)
    data = api.get()
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

def get_all_activities_time_range(athlete_id: int, before: int, after: int) -> list:
    api = Activity(athlete_id=athlete_id)
    data = api.get_all_activities(before=before, after=after)
    return data