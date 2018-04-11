# member.py
from data.database import SqlTools


class DataMembers:

    def __init__(self):
        self._sql = SqlTools()

        # def add_member(self):
        #     try:
        #         self._sql.query("""INSERT INTO members (invitecode, nickname, realname, idguild)
        #                     VALUES ('{0}',
        #                              '{1}', '{2}',
        #                             (select idguild
        #                                 from guilds
        #                                     where guildname = '{3}'))  """.format(self._inviteCode, self._nick,
        #                                                                           self._realName, self._guildName))
        # finally:
        #    if self._sql.conn:
        #        self._sql.conn.commit()
        #        self._sql.conn.close()


def cleanup_member_list(self, guild_name):
    try:
        self._sql.query(""" DELETE FROM members 
                                WHERE 
                                nickname not in 
                                    (SELECT UserName 
                                    FROM GoWDataDump x 
                                    WHERE 
                                    members.nickname = x.UserName)
                                and GuildName = '{0}' """.format(guild_name))
    finally:
        if self._sql.conn:
            self._sql.conn.commit()
            self._sql.conn.close()


def update_members(self):
    dump = self._sql.query("""SELECT * from GoWDataDump""")

    for row in dump:
        self._sql.query(""" UPDATE members set
                                    TrophiesTotal = {0},
                                    GoldTotal = {0},
                                    SealsTotal = {0},
                                     
                                    TrophiesCurrWK = {0},
                                    GoldCurrWK = {0},
                                    SealsCurrWk = {0},
                                    LastPlayed = {0},
                                    HeroLvL = {0},
                                    DaysInGuild = {0}
                                 WHERE
                                    nickname = ,""")
