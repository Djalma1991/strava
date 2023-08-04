from os import environ

import httpx

from db import Tokens, Activities, Athletes
from schema import AthletesModel, TokensModel, ActivitiesModel


class Auth:
    def __init__(self, athlete_id: int = None) -> None:
        self.athlete_id = athlete_id
        self._uri = "https://www.strava.com"
        self._params = {
            "client_id": environ["CLIENT_ID"],
            "client_secret": environ["CLIENT_SECRET"],
        }

    def _get_token(self):
        db = Tokens()
        return db.select(id=self.athlete_id)

    def _update_token(self, data: TokensModel) -> TokensModel:
        db = Tokens()
        if db.select(id=self.athlete_id):
            return db.update(data=data)
        return db.insert(data=data)

    def authorization_token(self, code: str) -> TokensModel:
        url = self._uri + "/oauth/token"
        params = {
            **self._params,
            "code": code,
            "grant_type": "authorization_code",
        }

        resp = httpx.post(url=url, params=params)
        id = resp.json().pop("athlete").get("id")
        data = TokensModel.parse_obj({"id": id, **resp.json()})

        self.athlete_id = data.id
        return self._update_token(data=data)

    def refresh_token(self) -> TokensModel:
        url = self._uri + "/oauth/token"
        token = self._get_token()
        params = {
            **self._params,
            "refresh_token": token.refresh_token,
            "grant_type": "refresh_token",
        }

        resp = httpx.post(url=url, params=params)
        data = TokensModel.parse_obj({"id": self.athlete_id, **resp.json()})
        return self._update_token(data=data)


class Athlete(Auth):
    def __init__(self, athlete_id: int = None) -> None:
        super().__init__(athlete_id)
        if not self._get_token():
            raise ValueError(
                (
                    "Your athlete don't grant access to our app.\n"
                    "Get the tokens using the Auth class with a valid "
                    "authorization code using the method authorization_token.\n"
                    "g.e.:\n"
                    ">>> auth = Auth()\n"
                    '>>> data = auth.authorization_token(code="xxxxxxxxxxxx")\n'
                    "Help: https://developers.strava.com/docs/authentication/\n"
                    "or use https://www.strava.com/oauth/authorize?"
                    "client_id=69072&response_type=code&"
                    "redirect_uri=http://localhost/exchange_token&"
                    "approval_prompt=force&"
                    "scope=read,activity:read,activity:read_all,activity:write,profile:read_all"
                )
            )
        self.token = self.refresh_token()

    def _get_athlete(self):
        db = Athletes()
        return db.select(id=self.athlete_id)
    
    def _update_athlete(self, data: AthletesModel) -> AthletesModel:
        db = Athletes()
        if db.select(id=self.athlete_id):
            return db.update(data=data)
        return db.insert(data=data)

    def get(self) -> AthletesModel:
        url = self._uri + "/api/v3/athlete"
        headers = {"Authorization": f"Bearer {self.token.access_token}"}
        resp = httpx.get(url=url, headers=headers)
        data = resp.json()
        data["strava_created_at"] = data.pop("created_at")
        data["strava_updated_at"] = data.pop("updated_at")
        data = AthletesModel.parse_obj(data)
        return self._update_athlete(data=data)

class Activity(Auth):
    def __init__(self, athlete_id: int = None, activity_id: int = None) -> None:
        super().__init__(athlete_id)
        self.activity_id = activity_id
        if not self._get_token():
            raise ValueError(
                (
                    "Your athlete don't grant access to our app.\n"
                    "Get the tokens using the Auth class with a valid "
                    "authorization code using the method authorization_token.\n"
                    "g.e.:\n"
                    ">>> auth = Auth()\n"
                    '>>> data = auth.authorization_token(code="xxxxxxxxxxxx")\n'
                    "Help: https://developers.strava.com/docs/authentication/\n"
                    "or use https://www.strava.com/oauth/authorize?"
                    "client_id=69072&response_type=code&"
                    "redirect_uri=http://localhost/exchange_token&"
                    "approval_prompt=force&"
                    "scope=read,activity:read,activity:read_all,activity:write,profile:read_all"
                )
            )
        self.token = self.refresh_token()

    def _update_activity(self, data: ActivitiesModel) -> ActivitiesModel:
            db = Activities()
            if db.select(id=self.activity_id):
                return db.update(data=data)
            return db.insert(data=data)

    def get(self) -> dict:
        url = self._uri + "/api/v3/activities/" + str(self.activity_id)
        headers = {"Authorization": f"Bearer {self.token.access_token}"}
        resp = httpx.get(url=url, headers=headers)
        temp = resp.json()
        id = temp.pop("id")
        temp["athlete"] = temp["athlete"].get("id")
        data = ActivitiesModel.parse_obj({"id": id, **temp})
        return self._update_activity(data=data)
    
    def get_all_activities(self, before, after) -> list:
        self.before = before
        self.after = after
        params = {
            **self._params,
            "before": before,
            "after": after,
            "per_page": 99
        }
        url = self._uri + "/api/v3/athlete/activities"
        headers = {"Authorization": f"Bearer {self.token.access_token}"}
        resp = httpx.get(url=url, headers=headers, params=params)
        temp = resp.json()
        ids = []
        i = 0
        while i < len(temp):
            ids.append(temp[i]["id"])
            temp[i].pop("id")
            i = i + 1
        return ids

        