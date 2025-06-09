from fastapi import FastAPI

from backend.api import users, quests, reviews
from backend.db import engine
from backend.models import Base

app = FastAPI(title="QHERO API")

app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(quests.router, prefix="/quests", tags=["quests"])
app.include_router(reviews.router, prefix="/reviews", tags=["reviews"])

@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
