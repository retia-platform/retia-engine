import logging

from apscheduler.schedulers.background import BackgroundScheduler

from src.retia_api import settings

scheduler = BackgroundScheduler()


def start():
    if settings.DEBUG:
        # Hook into the apscheduler logger
        logging.basicConfig()
        logging.getLogger("apscheduler").setLevel(logging.DEBUG)
