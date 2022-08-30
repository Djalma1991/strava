from api import Athlete
from db import Athletes, Tokens


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
