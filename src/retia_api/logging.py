from datetime import datetime, timezone

from src.retia_api.models import ActivityLog


def activity_log(severity, instance, category, messages):
    log = ActivityLog(
        time=datetime.now()
        .astimezone(tz=timezone.utc)
        .strftime("%Y-%m-%d %H:%M:%S %z"),
        severity=severity,
        instance=instance,
        category=category,
        messages=messages,
    )
    log.save()
