# settings.py

# a place for all the constants defines etc...

# Settings for Bot join
import discord.server

from data.database import SqlTools


class Settings:
    channel_results = ''
    channel_members = ''
    server = ''
    server_id = ''
    server_name = ''

    def __init(self):
        self.server = discord.Server()
        self.server_id = self.server.id
        self.server_name = self.server.name

    def get_channel_results(self):
        try:
            sql = SqlTools()
            cur = sql.query("""Select ChannelResults, ChannelMembers 
                         from settings where serverid = '{0}' """.format(self.server_id))
            if cur.rowcount > 0:
                row = cur.fetchone()
                self.channel_results = row[0]
                self.channel_members = row[1]
        finally:
            sql.conn.close()

    def get_channel_members(self):
        try:
            sql = SqlTools()
            cur = sql.query("""Select ChannelResults, ChannelMembers 
                         from settings where serverid = '{0}' """.format(self.server_id))
            if cur.rowcount > 0:
                row = cur.fetchone()
                self.channel_results = row[0]
                self.channel_members = row[1]
        finally:
            sql.conn.close()

    def set_channel_results(self, channelname):
        if self.channel_results == '':
            raise ValueError("""The variable 'channel_results' is empty. Please  """)

        try:
            sql = SqlTools()
            sql.query(""" update settings set ChannelResults = {0},
                                where serverid = {1}
                            """.format(self.channel_results, self.server_id))
            sql.conn.commit()
        finally:
            sql.conn.close()

    def set_channel_members(self, channelname):
        if self.channel_members == '':
            raise ValueError("""The variable 'channel_members' is empty. Please  """)

        try:
            sql = SqlTools()
            sql.query(""" update settings set ChannelMembers = {0}, 
                                where serverid = {1}
                            """.format(self.channel_members, self.server_id))
            sql.conn.commit()
        finally:
            sql.conn.close()
