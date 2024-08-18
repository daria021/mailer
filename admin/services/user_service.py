from dataclasses import dataclass

import httpx

from services.schemas import UserCreate, UserTagCreate, UserFilter, UserResponse


@dataclass
class UserService:
    host: str
    port: int

    @property
    def url(self):
        return f"http://{self.host}:{self.port}/user"

    async def create_user(self, schema: UserCreate):
        url = self.url
        async with httpx.AsyncClient() as client:
            response = await client.post(url, json={"email": schema.email, "hash_password": schema.hash_password})

        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    async def add_tag(self, schema: UserTagCreate):
        url = self.url + f"/tag"
        print("ASDFGHJKL<MNBVCXSDFGHJMNBVCFGHBVGHBVFGHJKJHGASDFGHJHGF")

        print(url)
        async with httpx.AsyncClient() as client:
            response = await client.post(url, json={"user": schema.user, "tag": schema.tag})

        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    async def get_all_users(self):
        url = self.url + "/all"
        async with httpx.AsyncClient() as client:
            response = await client.get(url)

        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    async def get_filtered_user(self, schema: UserFilter):
        url = self.url
        json = {
            "email": schema.email,
            "hash_password": schema.hash_password
        }
        async with httpx.AsyncClient() as client:
            response = await client.get(url, params=json)

        if response.status_code == 200:
            return UserResponse.model_validate(response.json())  # TODO !!!!
        else:
            response.raise_for_status()
