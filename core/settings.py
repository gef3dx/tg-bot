import os
from dataclasses import dataclass
from dotenv import load_dotenv


@dataclass
class Bots:
    bot_token: str


@dataclass
class Settings:
    bots: Bots


def get_settings():
    load_dotenv()
    return Settings(
        bots=Bots(
            bot_token=os.getenv('TG_TOKEN'),
        )
    )


settings = get_settings()
