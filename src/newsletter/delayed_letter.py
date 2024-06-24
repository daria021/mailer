from datetime import datetime

from fastapi_mail import MessageSchema, MessageType
from sqlalchemy.ext.asyncio import AsyncSession

from decoder import MessageSchemaEncoder
from newsletter import NewsletterRepo
from user_tag.repository import UserTagRepo
from celery_tasks.tasks import send_letter

import kombu.utils.json as json_utils


async def delayed_letter(session: AsyncSession, newsletter_id: int):
    newsletter = await NewsletterRepo.get(session=session, record_id=newsletter_id)

    message = MessageSchema(
        subject=newsletter.subject,
        recipients=await UserTagRepo.get_users_by_tag(session=session, tags=[x.text for x in newsletter.tags]),
        body=newsletter.text,
        subtype=MessageType.html
    )

    target_time = newsletter.target_time
    sleep = (target_time - datetime.now()).seconds if target_time else 0
    result = send_letter.apply_async((json_utils.dumps(message, cls=MessageSchemaEncoder),), countdown=sleep)
    print("i'm here")
    return result
