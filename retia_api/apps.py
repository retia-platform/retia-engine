from django.apps import AppConfig

from retia_api.configurations import settings


class RetiaApiConfig(AppConfig):
    name = "retia_api"

    def ready(self):
        from retia_api.configurations.scheduler import scheduler

        if settings.SCHEDULER_AUTOSTART:
            scheduler.start()
