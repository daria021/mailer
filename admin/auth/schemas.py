from pydantic import BaseModel

class Credentials(BaseModel):
    email: str
    hash_password: str

class Tokens(BaseModel):
    access_token: str
