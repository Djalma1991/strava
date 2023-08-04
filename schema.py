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
    name: str = None
    athlete: int = None
    resource_state: int = None
    distance: float = None
    moving_time: int = None
    elapsed_time: int = None
    total_elevation_gain: float = None
    type: str = None
    sport_type: str = None
    start_date: datetime = None
    start_date_local: datetime = None
    timezone: str = None
    location_city: str = None
    location_state: str = None
    location_country: str = None
    achievement_count: int = None
    kudos_count: int = None
    comment_count: int = None
    athlete_count: int = None
    visibility: str = None
    max_speed: float = None
    average_speed: float = None
    average_temp: float = None
    average_cadence: float = None
    average_watts: float = None
    weighted_average_watts: float = None
    kilojoules: float = None
    device_watts: int = None
    has_heartrate: bool = None
    elev_high: float = None
    elev_low: float = None
    calories: float = None
    segment_efforts: list = None
    laps: list = None
    stats_visibility: list = None
    device_name: str = None
    embed_token: str = None
    private_note: str = None
    pr_count: int = None
    description: str = None
    gear_id: str = None
    created_at: datetime = None
    updated_at: datetime = None

    class Config:
        orm_mode = True
        allow_population_by_field_name = True