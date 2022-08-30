from datetime import datetime

from pydantic import BaseModel, Field


class TokensModel(BaseModel):
    id: int
    token_type: str
    expires_at: int
    expires_in: int
    refresh_token: str
    access_token: str
    created_at: datetime = None
    updated_at: datetime = None

    class Config:
        orm_mode = True


class AthletesModel(BaseModel):
    id: int
    username: str = None
    firstname: str
    lastname: str
    city: str
    state: str
    sex: str
    premium: bool
    strava_created_at: datetime
    strava_updated_at: datetime
    follower_count: int
    friend_count: int
    measurement_preference: str
    ftp: int = None
    weight: float
    clubs: list
    bikes: list
    created_at: datetime = None
    updated_at: datetime = None

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
