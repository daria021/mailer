from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from routes.auth_routes import router as auth_router
from midlewares.auth_midleware import check_for_auth
from routes.newsletter_router import router as newsletter_router
from routes.tag_router import router as tag_router
from routes.user_router import router as user_router

app = FastAPI()

# Подключаем статику
app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(newsletter_router)
app.include_router(user_router)
app.include_router(tag_router)

app.include_router(auth_router)

app.middleware('http')(check_for_auth)


#
# @app.get("/admin/users")
# async def manage_users(request: Request):
#     return templates.TemplateResponse("admin/users.html", {"request": request, "users": users})
#
#
# @app.get("/admin/posts")
# async def manage_posts(request: Request):
#     return templates.TemplateResponse("admin/posts.html", {"request": request, "posts": posts})
