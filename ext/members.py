from discord.ext import commands

from data.datamembers import DataMembers


class Members:

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def add_member(self, pNick, pRealName, pInvitecode, pGuildname):
        mem = DataMembers(pNick, pRealName, pInvitecode, pGuildname)
        mem.add_member()
        await self.bot.say('Welcome @{0} we are glad to have you here in {1}'.format(pNick, pGuildname))


def setup(bot):
    bot.add_cog(Members(bot))
