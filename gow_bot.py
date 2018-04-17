from discord.ext import commands

from config.config import Config
from data.database import SqlTools

startup_extensions = ['ext.members', 'ext.guilds', 'ext.data']

config = Config('config/config.ini')
config.load_config()

bot = commands.Bot(config.cmd_prefix)


#
# EVENTS
#

@bot.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == bot.user:
        return

    await bot.process_commands(message)
    # if message.content.startswith('!hello'):
    #    msg = 'Hello {0.author.mention}'.format(message)
    #    await bot.send_message(message.channel, msg)

    # if message.content.startswith('!add_member'):
    #    msg = 'Hello {0.author.mention}'.format(message)
    #    await bot.send_message(message.channel, msg)


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    #     sql = SqlTools()
    #    output = sql.show_version()
    #   if output != '':
    #      print('Succesfully connected to the Database:  ' + output)
    print('------')
    servers = list(bot.servers)
    print("Connected on " + str(len(bot.servers)) + " servers")
    for x in range(len(servers)):
        print('    ' + servers[x - 1].name)
        if is_new_server(servers[x - 1].id) == 0:
            add_server(servers[x - 1].id, servers[x - 1].name)


#  finally:
#        if sql:
#           sql.conn.close()


#
# COMMANDS
#

@bot.command(pass_context=True)
async def hello(context):
    msg = 'Hello {0.author.mention}'.format(context.message)
    await bot.send_message(context.message.channel, msg)


#
# SETTING THINGS UP
#

def is_new_server(pServerid):
    try:
        sql = SqlTools()
        if sql:
            cur = sql.query('''Select serverid from settings where serverid = '{0}' '''.format(pServerid))
            return cur.rowcount
    finally:
        sql.conn.close()


def add_server(pServerId, pServerName):
    try:
        sql = SqlTools()
        if sql:
            cur = sql.query(
                '''INSERT INTO settings (serverid, servername) values ('{0}', '{1}')'''.format(pServerId, pServerName))
            # if cur.recordcount != 0:
            print('Added a new Server to the Database: ' + pServerId + ' - ' + pServerName)
    finally:
        if sql:
            sql.conn.commit()
            sql.conn.close()


if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

bot.run(config.token)
