from asgiref.sync import async_to_sync
import kombu.utils.json as json_utils
from fastapi_mail import FastMail, MessageSchema

from config import mail_conf
from .setup_celery import celery_app


@celery_app.task()
def send_letter(message: str):
    message = MessageSchema.model_validate(json_utils.loads(message))
    fm = FastMail(mail_conf)
    async_to_sync(fm.send_message)(message)
    return
