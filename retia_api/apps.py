from django.apps import AppConfig
from retia_api import settings


class RetiaApiConfig(AppConfig):
    name = "retia_api"

    def ready(self):
        from retia_api.scheduler import scheduler

        if settings.SCHEDULER_AUTOSTART:
            scheduler.start()
