from .schemas import Credentials


def auth_code_form(
        credentials: Credentials
) -> Credentials:
    return credentials