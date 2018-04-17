import codecs
import csv
from contextlib import closing

import MySQLdb
import requests

from config.config import Config

config = Config('./config/config.ini')
config.load_config()


class SqlTools:

    def __init__(self):
        self.conn = MySQLdb.connect(config.host, config.user, config.passwd, config.db)

    def connect(self):
        self.conn = MySQLdb.connect(config.host, config.user, config.passwd, config.db)

    def show_version(self):
        if self.conn:
            cursor = self.conn.cursor()
            cursor.execute("SELECT VERSION()")
            data = cursor.fetchone()
            return 'Database-Version ' + str(data)

    def query(self, sql):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute(sql)
            except (AttributeError, MySQLdb.OperationalError):
                self.connect()
                cursor = self.conn.cursor()
                cursor.execute(sql)
            return cursor

    def get_gowdatadump(self):

        gowdatadump = gowdatadump

    def fetch_data(self):
        url = "http://www.taransworld.com/guilds/Magix/main.pl?dl=1&col=abcdefghijklmnopqrstuvwxyz&dlToken=29iQIfd93oBVNWijH&showTime=1"
        # Api Links to csv for magix and enchanted. data is refreshed at 6 in the morning everyday
        # http://www.taransworld.com/guilds/Enchanted/main.pl?dl=1&col=abcdefghijklmnopqrstuvwxyz&dlToken=29iQIfd93oBVNWijH&showTime=1
        # Magix 6:00:00am
        # Enchanted  6:00:15am
        self.query('delete from GoWDataDump')
        self.conn.commit()
        with closing(requests.get(url, stream=True)) as r:
            reader = csv.reader(codecs.iterdecode(r.iter_lines(), 'utf-8'), delimiter=',', quotechar='"')
            # with open('GuildView.csv') as csvfile:
            #    reader = csv.reader(csvfile)
            next(reader, None)
            # reader = csv.reader(codecs.iterdecode(r.iter_lines(), 'utf-8'), delimiter=',', quotechar='"')
            for row in reader:
                self.query("""INSERT INTO GoWDataDump 

                              (Username,
                               GuildRank,
                               HeroLvl,
                               DaysInGuild,
                               LastPlayed,
                               KingdomLvl,
                               GoldTotal,
                               SealsTotal,
                               TrohpiesTotal,
                               GoldCurrWK,
                               SealsCurrWK,
                               TrohpiesCurrWK,
                               EventCurrWK,
                               Guildname
                              ) VALUES 
                              (
                               '{0}',
                                {1},
                                {2},
                                {3},
                                '{4}',
                                '{5}',
                                {6},
                                {7},
                                {8},
                                {9},
                                {10},
                                {11},
                                '{12}',
                                '{13}'

                              ) """.format(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8],
                                           row[9],
                                           row[10], row[11], row[12], 'Magix'))
                self.conn.commit()
