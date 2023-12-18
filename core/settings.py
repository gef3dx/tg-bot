import os
from dataclasses import dataclass
from dotenv import load_dotenv
from pathlib import Path


@dataclass
class Bots:
    bot_token: str
    admin_id: int
    base_path: Path
    db_path: str
    db_echo: bool


@dataclass
class Settings:
    bots: Bots


def get_settings():
    load_dotenv()
    return Settings(
        bots=Bots(
            bot_token=os.getenv('TG_TOKEN'),
            admin_id=int(os.getenv('ADMIN_ID')),
            base_path=Path(__file__).parent.parent,
            db_path=f"sqlite+aiosqlite:///db.sqlite3",
            db_echo=False,
        )
    )


settings = get_settings()
