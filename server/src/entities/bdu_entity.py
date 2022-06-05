import sqlalchemy

class _BduEntity:

  def __init__(self):
    self.__entity = sqlalchemy.Table(
      'bdu',
      sqlalchemy.MetaData(),
      sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
      sqlalchemy.Column('name', sqlalchemy.String(12), nullable=False),
      sqlalchemy.Column('cve', sqlalchemy.String(255), nullable=False),
      sqlalchemy.Column('cwe', sqlalchemy.String(255), nullable=False),
      sqlalchemy.Column('capec_high', sqlalchemy.String(255), nullable=False),
      sqlalchemy.Column('capec_medium', sqlalchemy.String(255), nullable=False),
      sqlalchemy.Column('capec_low', sqlalchemy.String(255), nullable=False),
      sqlalchemy.Column('capec_no_chance', sqlalchemy.String(255), nullable=False),
    )

  @property
  def get_entity(self):
    return self.__entity


bdu_entity = _BduEntity().get_entity
