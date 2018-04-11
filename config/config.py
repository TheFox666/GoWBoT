# config.py

# a place for all the constants defines etc...

# Settings for Bot join
import configparser


class ConfigFormatError(Exception):
    pass


class Config:
    # Bot-Settings
    token = ''
    invite_url = ''
    cmd_prefix = ''

    # Database-Settings
    host = ''
    user = ''
    passwd = ''
    db = ''

    # Channel-Settings
    channel_results = ''
    channel_members = ''

    def __init__(self, config_file):
        self.config_file = config_file

        self._config = configparser.ConfigParser()
        self._config.read(config_file, encoding='utf-8')

        config_sections = {'BotSettings', 'Database', 'Channels'}.difference(self._config.sections())
        if config_sections:
            raise ConfigFormatError("""Your config has an invalid format! Please recheck it. 
                                    The sections of the configfile need to be: 
                                    [BotSettings]
                                    .
                                    [Database]
                                    .
                                    [Channels]
                                    """)

    def load_config(self):
        self.token = self._config['BotSettings']['Token']
        self.invite_url = self._config['BotSettings']['InviteUrl']
        self.cmd_prefix = self._config['BotSettings']['CMDPrefix']

        self.host = self._config['Database']['Host']
        self.user = self._config['Database']['User']
        self.passwd = self._config['Database']['passwd']
        self.db = self._config['Database']['DB']

        self.channel_members = self._config['Channels']['Members']
        self.channel_results = self._config['Channels']['Results']
