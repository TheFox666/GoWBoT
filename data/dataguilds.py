from data.database import SqlTools


class DataGuild:
    """Stellt die Entität der Gilde dar"""

    def __init__(self, guildName):
        self._guildName = guildName

    def add_guild(self):
        try:
            sql = SqlTools()
            sql.query("""INSERT INTO guilds (guildname) 
                        VALUES ('{0}')  """.format(self._guildName))

        finally:
            if sql.conn:
                sql.conn.commit()
                sql.conn.close()
