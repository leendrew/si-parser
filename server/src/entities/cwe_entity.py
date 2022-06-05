import sqlalchemy

class _CweEntity:

  def __init__(self):
    self.__entity = sqlalchemy.Table(
      'cwe',
      sqlalchemy.MetaData(),
      sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
      sqlalchemy.Column('value', sqlalchemy.Integer, nullable=False, unique=True),
    )

  @property
  def get_entity(self):
    return self.__entity


cwe_entity = _CweEntity().get_entity
