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


class ActivitiesModel(BaseModel):
    id: int
    name: str
    athlete: int
    resource_state: int
    distance: float
    moving_time: int
    elapsed_time: int
    total_elevation_gain: float
    type: str
    sport_type: str
    start_date: datetime
    start_date_local: datetime
    timezone: str
    location_city: str = None
    location_state: str = None
    location_country: str
    achievement_count: int
    kudos_count: int
    comment_count: int
    athlete_count: int
    visibility: str
    max_speed: float
    average_speed: float
    average_temp: float = None
    average_cadence: float
    average_watts: float
    weighted_average_watts: float
    kilojoules: float
    device_watts: int
    has_heartrate: bool
    elev_high: float = None
    elev_low: float = None
    calories: float
    segment_efforts: list
    laps: list
    stats_visibility: list
    device_name: str
    embed_token: str
    private_note: str
    pr_count: int
    description: str
    gear_id: str = None
    created_at: datetime = None
    updated_at: datetime = None

    class Config:
        orm_mode = True
        allow_population_by_field_name = True