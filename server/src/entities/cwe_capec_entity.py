import sqlalchemy

class _CweCapecEntity:

  def __init__(self):
    self.__entity = sqlalchemy.Table(
      'cwe_capec',
      sqlalchemy.MetaData(),
      sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
      sqlalchemy.Column('cwe_id', sqlalchemy.Integer, sqlalchemy.ForeignKey('cwe.id'), nullable=False),
      sqlalchemy.Column('capec_id', sqlalchemy.Integer, sqlalchemy.ForeignKey('capec.id'), nullable=False),
    )

  @property
  def get_entity(self):
    return self.__entity


cwe_capec_entity = _CweCapecEntity().get_entity
