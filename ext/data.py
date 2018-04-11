from discord.ext import commands
from settings import Settings

from data.database import SqlTools


class Data:

    def __init__(self, bot):
        self.bot = bot
        self.setup = Settings()
        self.setup.load_settings()

    @commands.command()
    async def fetch_data(self):
        db = SqlTools()
        db.fetch_data()
        await self.bot.say('Data has been fetched like crazy!!!')

    @commands.command(name="SetMemberChannel")
    async def set_member_channel(self, channelname):
        self.setup.set_channel_members(channelname)
        await self.bot.say('New Member Channel {0} has been set!'.format(channelname))

    @commands.command(name="SetResultsChannel")
    async def set_results_channel(self, channelname):
        self.setup.set_channel_results(channelname)
        await self.bot.say('New Results Channel {0} has been set!'.format(channelname))

    @commands.command()
    async def fetch_data(self):
        db = SqlTools()
        db.fetch_data()
        await self.bot.say('Data has been fetched like crazy!!!')


def setup(bot):
    bot.add_cog(Data(bot))
