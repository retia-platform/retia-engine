from django.apps import AppConfig

from src.retia_api import settings


class RetiaApiConfig(AppConfig):
    name = "src.retia_api"

    def ready(self):
        from src.retia_api.scheduler import scheduler

        if settings.SCHEDULER_AUTOSTART:
            scheduler.start()
