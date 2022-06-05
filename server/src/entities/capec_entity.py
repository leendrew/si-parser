import sqlalchemy
from enum import Enum

class CAPEC_TYPE(Enum):
  HIGH = 'high',
  MEDIUM = 'medium',
  LOW = 'low',
  NO_CHANCE = 'no_chance'

class _CapecEntity:

  def __init__(self):
    self.__entity = sqlalchemy.Table(
      'capec',
      sqlalchemy.MetaData(),
      sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
      sqlalchemy.Column('value', sqlalchemy.Integer, nullable=False, unique=True),
      sqlalchemy.Column('type', sqlalchemy.Enum(CAPEC_TYPE), nullable=False),
    )

  @property
  def get_entity(self):
    return self.__entity


capec_entity = _CapecEntity().get_entity
