from sqlalchemy import MetaData, Column, Integer, String, ForeignKey, SmallInteger
from app.db import Base

# data generated by Ander's LibTech3


class ParsedPlayer(Base):
    __tablename__ = 'player'
    id = Column('dwSeq', Integer(), primary_key=True)
    szMd5 = Column(String(32), nullable=False, index=True)
    szName = Column(String(128), nullable=False)
    szCleanName = Column(String(64), nullable=False)
    bClientNum = Column(SmallInteger(), nullable=False)
    szInfoString = Column(String(256), nullable=False)
    bTeam = Column(SmallInteger(), nullable=False)
    bTVClient = Column(SmallInteger(), nullable=False)


class ParsedRoundStast(Base):
    __tablename__ = 'roundstats'
    id = Column('dwSeq', Integer(), primary_key=True)
    szMd5 = Column(String(32), nullable=False, index=True)
    bRound = Column(String(128), nullable=False)
    szTimeToBeat = Column(String(32), nullable=False)
    szStats = Column(String(512), nullable=False)
