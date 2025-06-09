from datetime import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime, JSON
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    nickname = Column(String, nullable=False)
    avatar = Column(String)
    genres = Column(JSON)
    xp = Column(Integer, default=0)
    level = Column(Integer, default=1)
    rating_profile = Column(Integer, default=0)
    area = Column(String)

    records = relationship('Record', back_populates='user')
    achievements = relationship('UserAchievement', back_populates='user')

class Quest(Base):
    __tablename__ = 'quests'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    genre = Column(String)
    characteristics = Column(JSON)
    rating = Column(Integer, default=0)
    price = Column(Integer)
    location = Column(String)
    has_discount = Column(Boolean, default=False)

    records = relationship('Record', back_populates='quest')

class Record(Base):
    __tablename__ = 'records'
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    quest_id = Column(Integer, ForeignKey('quests.id'), primary_key=True)
    confirmed = Column(Boolean, default=False)
    scanned_at = Column(DateTime)

    user = relationship('User', back_populates='records')
    quest = relationship('Quest', back_populates='records')

class Review(Base):
    __tablename__ = 'reviews'
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    quest_id = Column(Integer, ForeignKey('quests.id'), primary_key=True)
    rating = Column(Integer)
    comment = Column(String)
    weight = Column(Integer)
    genre_match = Column(Integer)

class Achievement(Base):
    __tablename__ = 'achievements'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String)
    xp_reward = Column(Integer)

class UserAchievement(Base):
    __tablename__ = 'user_achievements'
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    achievement_id = Column(Integer, ForeignKey('achievements.id'), primary_key=True)
    received_at = Column(DateTime, default=datetime.utcnow)

    user = relationship('User', back_populates='achievements')
