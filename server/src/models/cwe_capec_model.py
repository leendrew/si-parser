from pydantic import BaseModel

class BduBase(BaseModel):
  value: int

class Bdu(BduBase):
  id: int

  class Config:
    orm_mode = True
