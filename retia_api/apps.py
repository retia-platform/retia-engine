from django.apps import AppConfig

from retia_api.configurations import settings
from retia_api.configurations.scheduler import scheduler


class RetiaApiConfig(AppConfig):
    name = "retia_api"

    def ready(self):
        if settings.SCHEDULER_AUTOSTART:
            scheduler.start()
