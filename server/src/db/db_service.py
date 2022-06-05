from databases import Database
from src.config.config_service import config_service

class _DBService:

  def __init__(self):
    self.db = Database(config_service.POSTGRES_URL)

  async def connect(self):
    await self.db.connect()

  async def disconnect(self):
    await self.db.disconnect()

db_service = _DBService()
