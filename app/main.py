from fastapi import FastAPI
from app.routers.is_user_subscribed import router

app = FastAPI(title="Telegram Subscription Checker")
app.include_router(router)
