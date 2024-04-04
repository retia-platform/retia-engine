from apscheduler.schedulers.background import BackgroundScheduler
import retia_api.settings

scheduler = BackgroundScheduler(retia_api.settings.SCHEDULER_CONFIG)