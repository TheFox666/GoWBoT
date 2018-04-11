# member.py
from data.database import SqlTools


class DataMembers:

    def __init__(self):
        self._sql = SqlTools()

    def add_member(self):
        try:
            self._sql.query("""INSERT INTO members (invitecode, nickname, realname, idguild) 
                        VALUES ('{0}', 
                                 '{1}', '{2}',
                                (select idguild 
                                    from guilds 
                                        where guildname = '{3}'))  """.format(self._inviteCode, self._nick,
                                                                              self._realName, self._guildName))
        finally:
            if self._sql.conn:
                self._sql.conn.commit()
                self._sql.conn.close()
