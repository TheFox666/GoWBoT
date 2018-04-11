from discord.ext import commands

from data.dataguilds import DataGuild


class Guilds:

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def add_guild(self, guildname):
        guild = DataGuild(guildname)
        guild.add_guild()
        await self.bot.say('Guild {0} has been added!'.format(guildname))


def setup(bot):
    bot.add_cog(Guilds(bot))
