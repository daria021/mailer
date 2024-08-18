import kombu.utils.json as json_utils
from fastapi_mail import MessageSchema


class MessageSchemaEncoder(json_utils.JSONEncoder):
    def default(self, o):
        if isinstance(o, MessageSchema):
            return {
                "subject": o.subject,
                "recipients": o.recipients,
                "body": o.body,
                "subtype": o.subtype.value,
            }
        return super().default(o)
