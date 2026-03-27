from datetime import datetime, timezone, timedelta

def get_current_utc_time():
    return datetime.now(timezone.utc)

def get_time_24_hours_ago():
    return get_current_utc_time() - timedelta(days=1)
