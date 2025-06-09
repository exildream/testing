from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from backend.db import get_session
from backend.models import Review

router = APIRouter()

@router.get('/quest/{quest_id}')
async def quest_reviews(quest_id: int, session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Review).where(Review.quest_id == quest_id))
    return result.scalars().all()
