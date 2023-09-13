from api import Athlete, Activity
from db import Tokens, Activities
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

def get_all_activities_time_range(athlete_id: int, before: int = None, after: int = None) -> list:
    api = Activity(athlete_id=athlete_id)
    data = api.get_all_activities(before=before, after=after)
    return data

def update_gear_in_strava(athlete_id: int, gear_id: str):
    db = Activities()
    app = Activity(athlete_id=athlete_id)
    data = db.select_activities_without_gear(ride='Ride')
    activities_to_update = []
    for _ in data:
        activities_to_update.append(
            {"id": _.id,
             "gear_id": gear_id}
        )
    for activity in activities_to_update:
        app.update_activity(id=activity["id"], 
                            data={"gear_id": activity["gear_id"]})
    return data