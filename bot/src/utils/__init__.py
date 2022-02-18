import os

from datetime import datetime, timezone, timedelta


def get_current_time() -> datetime:
    return datetime.now(
        timezone(
            timedelta(hours=3), 
            name=os.environ.get('TIMEZONE', None)
        )
    )
