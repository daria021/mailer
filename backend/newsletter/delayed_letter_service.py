import threading

import kombu.utils.json as json_utils
from fastapi_mail import MessageSchema, MessageType

from celery_tasks.tasks import send_letter
from decoder import MessageSchemaEncoder
from newsletter.dependencies.repositories import get_newsletter_repo
from user_tag.dependencies.services import get_user_tag_service


async def delayed_letter(
        newsletter_id: int,
):
    newsletters = get_newsletter_repo()
    newsletter = await newsletters.get(obj_id=newsletter_id)

    user_tags_service = get_user_tag_service()
    recipients = await user_tags_service.get_users_by_tag(tags=[x.text for x in newsletter.tags])

    def send_to_recipient(recipient):
        message = MessageSchema(
            subject=newsletter.subject,
            recipients=[recipient],
            body=newsletter.text,
            subtype=MessageType.html
        )
        result = send_letter.apply_async((json_utils.dumps(message, cls=MessageSchemaEncoder),), countdown=0)
        return result

    threads = []
    for recipient in recipients:
        thread = threading.Thread(target=send_to_recipient, args=(recipient,), name=f"send letter to {recipient}")
        thread.start()
        threads.append(thread)

    for thread in threading.enumerate():
        print(f"Active thread: {thread.name}")

    for thread in threads:
        thread.join()

    print("All emails sent.")
