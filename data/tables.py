from base import Base, Session, engine
from sqlalchemy import Column, String, Integer, Date, DateTime



class GoWDatadump(Base):
    __tablename__ = 'gowdatadump'

    DataID = Column(Integer, primary_key=True)
    UserName = Column(String)
    GuildRank = Column(Integer)
    HeroLvL = Column(Integer)
    DaysInGuild = Column(Integer)
    LastPlayed = Column(String)
    GoldTotal = Column(Integer)
    SealsTotal = Column(Integer)
    TrohpiesTotal = Column(Integer)
    GoldCurrWK = Column(Integer)
    SealsCurrWK = Column(Integer)
    TrophiesCurrWK = Column(Integer)
    Guildname = Column(String)

    def __init__(self, username, guild_rank, hero_lvl, days_in_guild, last_played, gold_total,
                 seals_total, trophies_total, gold_curr_wk, seals_curr_wk, trohpies_curr_wk,
                 guild_name
                ):
        self.UserName = username
        self.GuildRank = guild_rank
        self.HeroLvL = hero_lvl
        self.DaysInGuild = days_in_guild
        self.LastPlayed = last_played
        self.GoldTotal = gold_total
        self.SealsTotal = seals_total
        self.TrohpiesTotal = trophies_total
        self.GoldCurrWK = gold_curr_wk
        self.SealsCurrWK = seals_curr_wk
        self.TrophiesCurrWK = trohpies_curr_wk
        self.Guildname = guild_name

    def del_gowdatadump(self):
        session = Session()

        session.

class Members(Base):
    __tablename__ = 'members'

    nickname = Column(String, primary_key=True)
    invitecode = Column(String)
    realname = Column(String)
    JoinDate = Column(DateTime)
    HeroLvL = Column(Integer)
    DaysInGuild = Column(Integer)
    LastPlayed = Column(String)
    GoldTotal = Column(Integer)
    SealsTotal = Column(Integer)
    TrohpiesTotal = Column(Integer)
    GoldCurrWK = Column(Integer)
    SealsCurrWK = Column(Integer)
    TrophiesCurrWK = Column(Integer)
    Guildname = Column(String)
