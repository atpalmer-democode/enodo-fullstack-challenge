from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_ENGINE_CONFIG = {
    'name_or_url': 'sqlite:///./data/rawdata.db',
    'echo': True,
}


Session = sessionmaker(bind=create_engine(**SQLALCHEMY_ENGINE_CONFIG))

