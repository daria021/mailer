import celery_decorator_taskcls
from celery import Celery

from config import config

celery_decorator_taskcls.patch_celery()

celery_app = Celery('celery', broker=config.redis_url)
