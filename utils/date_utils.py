from datetime import datetime, timedelta
from typing import Optional

def format_iso_datetime(dt: Optional[datetime] = None) -> str:
    """
    Return the current or provided datetime in ISO 8601 format.
    """
    dt = dt or datetime.utcnow()
    return dt.isoformat() + 'Z'

def add_business_days(start_date: datetime, days: int) -> datetime:
    """
    Add business days (Monday-Friday) to a date.
    """
    current_date = start_date
    while days > 0:
        current_date += timedelta(days=1)
        if current_date.weekday() < 5:  # Monday to Friday are 0-4
            days -= 1
    return current_date
