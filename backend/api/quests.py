from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from backend.db import get_session
from backend.models import Quest

router = APIRouter()

@router.get('/')
async def list_quests(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Quest).limit(20))
    return result.scalars().all()
