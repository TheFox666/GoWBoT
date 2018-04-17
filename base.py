from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta
from sqlalchemy.orm import sessionmaker
from config.config import Config

config = Config('./config/config.ini')
config.load_config()

engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(config.user, config.passwd, config.host, config.db))
Session = sessionmaker(bind=engine)

Base = declarative_base()
