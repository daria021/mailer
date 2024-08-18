from dataclasses import dataclass

import httpx

from services.schemas import TagCreate


@dataclass
class TagService:
    host: str
    port: int

    @property
    def url(self):
        return f"http://{self.host}:{self.port}/tag"

    async def add_tag(self, schema: TagCreate):
        url = self.url
        async with httpx.AsyncClient() as client:
            response = await client.post(url, json={"text": schema.text})

        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    async def get_all_tags(self):
        url = self.url + "/all"
        async with httpx.AsyncClient() as client:
            response = await client.get(url)

        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()
