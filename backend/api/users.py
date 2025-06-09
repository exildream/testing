from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from backend.db import get_session
from backend.models import User

router = APIRouter()

@router.get("/{tg_id}")
async def get_user(tg_id: int, session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(User).where(User.id == tg_id))
    user = result.scalar_one_or_none()
    return user
