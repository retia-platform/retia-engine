import logging

from apscheduler.schedulers.background import BackgroundScheduler

from retia_api.configurations import settings

scheduler = BackgroundScheduler()


def start():
    if settings.DEBUG:
        # Hook into the apscheduler logger
        logging.basicConfig()
        logging.getLogger("apscheduler").setLevel(logging.DEBUG)
