from dataclasses import dataclass

import httpx

from services.schemas import NewsletterCreate, NewsletterFilter


@dataclass
class NewsletterService:
    host: str
    port: int

    @property
    def url(self):
        return f"http://{self.host}:{self.port}/newsletter"

    async def create_newsletter(self, schema: NewsletterCreate):
        url = self.url

        json = {
            "user": schema.user,
            "subject": schema.subject,
            "text": schema.text,
            "target_time": schema.target_time.strftime("%Y-%m-%d %H:%M:%S"),
        }
        print(json)
        async with httpx.AsyncClient() as client:
            response = await client.post(
                url,
                json=json,
            )

        if response.status_code == 200:
            return response.json()
        else:
            print(response.content)
            response.raise_for_status()

    async def delete_newsletter(self, newsletter_id: int):
        url = self.url + f"/{newsletter_id}"
        print(url)

        async with httpx.AsyncClient() as client:
            response = await client.delete(url)

        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    async def get_all_newsletter(self):
        url = self.url
        async with httpx.AsyncClient() as client:
            response = await client.get(url)

        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    async def get_one(self, newsletter_id: int):
        url = self.url + f"/{newsletter_id}"
        async with httpx.AsyncClient() as client:
            response = await client.get(url)

        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    async def get_filtered_newsletter(self, schema: NewsletterFilter):
        url = self.url

        async with httpx.AsyncClient() as client:
            response = await client.get(url, params=schema.dict())

        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()
