from datetime import datetime
from os import environ
from select import select

import sqlalchemy

from schema import AthletesModel, TokensModel

metadata = sqlalchemy.MetaData()


class DB:
    def __init__(self):
        self.uri = environ["DB_URI"]
        self.engine = sqlalchemy.create_engine(self.uri)
        self.conn = self.engine.connect()
        self.conn.execution_options(isolation_level="AUTOCOMMIT", autocommit=True)

    def __del__(self):
        if not self.conn.closed:
            self.conn.close()


tokens = sqlalchemy.Table(
    "tokens",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.INT, primary_key=True, autoincrement=False),
    sqlalchemy.Column("token_type", sqlalchemy.VARCHAR),
    sqlalchemy.Column("expires_at", sqlalchemy.BIGINT),
    sqlalchemy.Column("expires_in", sqlalchemy.BIGINT),
    sqlalchemy.Column("refresh_token", sqlalchemy.VARCHAR),
    sqlalchemy.Column("access_token", sqlalchemy.VARCHAR),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime, default=datetime.now),
    sqlalchemy.Column(
        "updated_at", sqlalchemy.DateTime, default=datetime.now, onupdate=datetime.now
    ),
)


class Tokens(DB):
    def __init__(self):
        super().__init__()
        self.tokens: sqlalchemy.Table = tokens
        metadata.create_all(bind=self.engine)

    def insert(self, data: TokensModel) -> TokensModel:
        row = self.tokens.insert().values(**data.dict(exclude_none=True))
        self.conn.execute(row)
        return self.select(id=data.id)

    def update(self, data: TokensModel) -> TokensModel:
        row = (
            self.tokens.update()
            .where(self.tokens.c.id == data.id)
            .values(**data.dict(exclude={"id"}, exclude_none=True))
        )
        self.conn.execute(row)
        return self.select(id=data.id)

    def select(self, id: int) -> TokensModel:
        item = self.tokens.select().where(self.tokens.c.id == id)
        result = self.conn.execute(item).first()
        return TokensModel.from_orm(result) if result else None


athletes = sqlalchemy.Table(
    "athletes",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.INT, primary_key=True, autoincrement=False),
    sqlalchemy.Column("username", sqlalchemy.VARCHAR),
    sqlalchemy.Column("firstname", sqlalchemy.VARCHAR),
    sqlalchemy.Column("lastname", sqlalchemy.VARCHAR),
    sqlalchemy.Column("city", sqlalchemy.VARCHAR),
    sqlalchemy.Column("state", sqlalchemy.VARCHAR),
    sqlalchemy.Column("sex", sqlalchemy.VARCHAR),
    sqlalchemy.Column("premium", sqlalchemy.BOOLEAN),
    sqlalchemy.Column("strava_created_at", sqlalchemy.DateTime),
    sqlalchemy.Column("strava_updated_at", sqlalchemy.DateTime),
    sqlalchemy.Column("follower_count", sqlalchemy.INT),
    sqlalchemy.Column("friend_count", sqlalchemy.INT),
    sqlalchemy.Column("measurement_preference", sqlalchemy.VARCHAR),
    sqlalchemy.Column("ftp", sqlalchemy.INT),
    sqlalchemy.Column("weight", sqlalchemy.NUMERIC(10, 4)),
    sqlalchemy.Column("clubs", sqlalchemy.JSON),
    sqlalchemy.Column("bikes", sqlalchemy.JSON),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime, default=datetime.now),
    sqlalchemy.Column(
        "updated_at", sqlalchemy.DateTime, default=datetime.now, onupdate=datetime.now
    ),
)


class Athletes(DB):
    def __init__(self):
        super().__init__()
        self.athletes: sqlalchemy.Table = athletes
        metadata.create_all(bind=self.engine)

    def insert(self, data: AthletesModel) -> AthletesModel:
        valid = data.dict(exclude_none=True, by_alias=False)
        row = self.athletes.insert().values(valid)
        self.conn.execute(row)
        return self.select(id=data.id)

    def update(self, data: AthletesModel) -> AthletesModel:
        row = (
            self.athletes.update()
            .where(self.athletes.c.id == data.id)
            .values(**data.dict(exclude={"id"}, exclude_none=True))
        )
        self.conn.execute(row)
        return self.select(id=data.id)

    def select(self, id: int) -> AthletesModel:
        item = self.athletes.select().where(self.athletes.c.id == id)
        result = self.conn.execute(item).first()
        return AthletesModel.from_orm(result) if result else None
