from sqlalchemy import Column, Integer, String, ForeignKey, Date, Boolean, Table
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    nickname = Column(String, nullable=False)
    avatar = Column(String)
    genres = Column(String)
    xp = Column(Integer, default=0)
    level = Column(Integer, default=1)
    rating_profile = Column(Integer, default=0)
    area = Column(String)
    achievements = relationship('UserAchievement', back_populates='user')

class Quest(Base):
    __tablename__ = 'quests'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    genres = Column(String)
    rating = Column(Integer, default=0)
    price = Column(Integer)
    features = Column(String)
    area = Column(String)
    active_qr_code = Column(String)

class Review(Base):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    quest_id = Column(Integer, ForeignKey('quests.id'))
    score = Column(Integer)
    weight = Column(Integer)
    genre_match = Column(Integer)
    text = Column(String)

class Achievement(Base):
    __tablename__ = 'achievements'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    xp_value = Column(Integer, default=0)
    icon = Column(String)

class UserAchievement(Base):
    __tablename__ = 'user_achievements'
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    achievement_id = Column(Integer, ForeignKey('achievements.id'), primary_key=True)
    date = Column(Date)
    user = relationship('User', back_populates='achievements')

class Record(Base):
    __tablename__ = 'records'
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    quest_id = Column(Integer, ForeignKey('quests.id'), primary_key=True)
    date = Column(Date)
    qr_verified = Column(Boolean, default=False)

class HotDeal(Base):
    __tablename__ = 'hot_deals'
    quest_id = Column(Integer, ForeignKey('quests.id'), primary_key=True)
    discount_percent = Column(Integer)
    valid_until = Column(Date)

