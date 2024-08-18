from fastapi import FastAPI
from newsletter import router as newsletter_router
from user import router as user_router
from tags import router as tag_router

app = FastAPI(
    title="newsletter"
)

app.include_router(newsletter_router)
app.include_router(user_router)
app.include_router(tag_router)

import logging

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    handlers=[
        logging.StreamHandler(),
    ]
)
