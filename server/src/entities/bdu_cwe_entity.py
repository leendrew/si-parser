import sqlalchemy

class _BduCweEntity:

  def __init__(self):
    self.__entity = sqlalchemy.Table(
      'bdu_cwe',
      sqlalchemy.MetaData(),
      sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
      sqlalchemy.Column('bdu_id', sqlalchemy.Integer, sqlalchemy.ForeignKey('bdu.id'), nullable=False),
      sqlalchemy.Column('cwe_id', sqlalchemy.Integer, sqlalchemy.ForeignKey('cwe.id'), nullable=False),
    )

  @property
  def get_entity(self):
    return self.__entity


bdu_cwe_entity = _BduCweEntity().get_entity
